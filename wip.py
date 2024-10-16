from pipin import install_requirements
install_requirements()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Professional quality webcam URL gatherer with enhanced features

import requests
import logging
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# URL of the website to scrape webcams from
base_url = "https://www.webcamtaxi.com/en/webcams.html"

# Custom headers for the request to mimic a real browser
headers = CaseInsensitiveDict({
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
})

# Retry settings
RETRY_COUNT = 3
RETRY_DELAY = 5  # seconds

# Function to scrape webcams with retry logic
def scrape_webcams():
    for attempt in range(RETRY_COUNT):
        try:
            logging.info(f"Sending request to fetch webcam data... (Attempt {attempt + 1}/{RETRY_COUNT})")
            response = requests.get(base_url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses

            soup = BeautifulSoup(response.text, "html.parser")

            # Gather all webcam links
            webcam_links = []
            for link in soup.find_all('a', href=True):
                if "webcams.html" in link['href']:  # Filter for main webcam links
                    full_url = f"https://www.webcamtaxi.com{link['href']}"
                    webcam_links.append(full_url)

                # Additionally check for specific cam links as per your request
                elif "/en/" in link['href'] and "cam" in link['href']:
                    full_url = f"https://www.webcamtaxi.com{link['href']}"
                    if full_url not in webcam_links:  # Prevent duplicates
                        webcam_links.append(full_url)

            if not webcam_links:
                logging.warning("No webcam links found.")
                return

            # Option to preview random webcams
            preview_random_webcams(webcam_links)

            # Save URLs by category
            save_urls_by_category(webcam_links)

            logging.info(f"Webcam URLs successfully saved to categorized files.")

            break  # Exit loop if successful

        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}. Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
    else:
        logging.error(f"Failed to fetch data after {RETRY_COUNT} attempts.")

# Function to preview random webcam streams
def preview_random_webcams(webcam_links):
    import random
    preview_count = 3
    preview_links = random.sample(webcam_links, min(preview_count, len(webcam_links)))

    for idx, link in enumerate(preview_links):
        print(f"Previewing random webcam {idx + 1}: {link}")
        open_in_browser(link)

# Function to open a stream in the browser
def open_in_browser(link):
    import webbrowser
    logging.info(f"Opening {link} in web browser...")
    webbrowser.open(link)

# Function to categorize and save webcam URLs
def save_urls_by_category(webcam_links):
    categories = {"Nature": [], "City": [], "Traffic": []}  # Example categories
    for link in webcam_links:
        # Simple categorization based on URL content (adjust as needed)
        if "nature" in link:
            categories["Nature"].append(link)
        elif "city" in link:
            categories["City"].append(link)
        else:
            categories["Traffic"].append(link)

    # Save categorized URLs to separate files
    for category, links in categories.items():
        if links:
            with open(f'{category.lower()}_webcams.txt', 'w') as file:
                for webcam_url in links:
                    file.write(webcam_url + '\n')
            logging.info(f"{category} webcams saved to {category.lower()}_webcams.txt.")

if __name__ == "__main__":
    scrape_webcams()
