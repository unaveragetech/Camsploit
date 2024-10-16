from pipin import install_requirements
install_requirements()

import streamlit as st
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # New import for Selenium element location
import os
import cv2
from time import sleep
from multiprocessing import Process
import tempfile
from io import BytesIO
from PIL import Image

# URLs and pictures list
urls = []
pics = []

# global setup for selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)

# Function to clear the terminal (no longer needed in Streamlit)
def cls():
    pass

# Streamlit header and logo
def header():
    st.markdown(
        """
        <h1 style="text-align: center; color: white;">
        🛠️ CCTV Stream Viewer 🛠️
        </h1>
        <h2 style="text-align: center; color: lightblue;">
        By: BLUND3R
        </h2>
        """, 
        unsafe_allow_html=True
    )

# HUD for displaying background activity
def hud(status_message):
    st.sidebar.write(f"### Status: {status_message}")
    st.sidebar.progress(0)

# Function to display streams
def display_stream(stream_link):
    try:
        cap = cv2.VideoCapture(stream_link)
        ret, frame = cap.read()

        if ret:
            # Save the frame to a temporary file and display it using Streamlit
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
            cv2.imwrite(temp_file.name, frame)
            cap.release()

            image = Image.open(temp_file.name)
            st.image(image, caption=f"Streaming from {stream_link}")
        else:
            st.warning(f"Failed to capture stream from {stream_link}")
    except Exception as e:
        st.error(f"Failed to display stream: {e}")

# Function to check URL status
def check_status(url):
    try:
        r = requests.get(url, timeout=10)
        return r.status_code == 200
    except:
        return False

# Function to run a query and collect streams
def run_query(query):
    hud("Starting Google search")
    driver.get("https://www.google.com/search?q=inurl:" + query)
    sleep(1)

    st.info("Loading... Please be patient, it can take a while to connect to cameras...")
    
    # Get all search results
    hud("Fetching search results")
    results = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']//a")  # Updated with By.XPATH
    
    # Collect URLs and verify stream
    for result in results:
        url = result.get_attribute('href')
        urls.append(url)
        hud(f"Checking {url}")
        if check_status(url):
            driver.get(url)
            loaded = False
            hud(f"Loading {url}")
            while not loaded:
                if driver.execute_script("return document.readyState") == "complete":
                    loaded = True
            
            try:
                # Extract stream link via JavaScript
                stream_link = driver.execute_script("""
                var imgs = document.querySelectorAll('img');
                var elem = '';
                var streamWidth = 0, streamHeight = 0;
                
                for (var i = 0; i < imgs.length; i++) {
                    if (imgs[i].clientWidth > streamWidth && imgs[i].clientHeight > streamHeight) {
                        elem = imgs[i].src;
                        streamWidth = imgs[i].clientWidth;
                        streamHeight = imgs[i].clientHeight;
                    }
                }
                return elem;
                """)
                if stream_link:
                    pics.append(stream_link)
                    display_stream(stream_link)
            except Exception as e:
                st.error(f"Error in stream capture: {e}")

    hud("Completed stream collection")

# Function to handle preset queries
def presets():
    st.write("## Select a preset query string")
    
    option = st.selectbox("Choose a query option", [
        "/view.shtml", "/view/index.shtml", "/mjpg/video.mjpg", "/cgi-bin/camera?resolution=", "Go back"
    ])
    
    if option == "Go back":
        start_screen()
    else:
        run_query(option)

# Start screen and main interaction menu
def start_screen():
    header()

    option = st.radio(
        "Select an option to begin:",
        ("Choose a preset query string", "Use a custom query string", "Exit")
    )
    
    if option == "Choose a preset query string":
        presets()
    elif option == "Use a custom query string":
        custom_query = st.text_input("Enter custom query string:")
        if custom_query:
            run_query(custom_query)
    elif option == "Exit":
        st.write("Goodbye!")
        st.stop()

# Start the app
if __name__ == "__main__":
    start_screen()
