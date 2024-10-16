from pipin import install_requirements
install_requirements()

import os
import sys
import logging
import webbrowser
import time
from datetime import datetime
import random

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Global dictionaries for quick links and tagging
quick_links = {}
tagged_links = {}

# Function to load webcam URLs from a selected directory
def load_webcam_links(directory='.'):
    file_name = 'traffic_webcams.txt'
    file_path = os.path.join(directory, file_name)
    
    if not os.path.exists(file_path):
        logging.error(f"'{file_name}' not found in {directory}.")
        return []
    
    try:
        with open(file_path, 'r') as f:
            links = [line.strip() for line in f.readlines() if line.strip()]
        return list(set(links))  # Remove duplicates
    except Exception as e:
        logging.error(f"Failed to read '{file_name}': {e}")
        return []

# Function to log visited links with a timestamp
def log_visited_link(link):
    with open('visited_links.txt', 'a') as f:
        f.write(f"{link} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Function to load visited links
def load_visited_links():
    if os.path.exists('visited_links.txt'):
        with open('visited_links.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    return []

# Function to save favorite links to 'favorites.txt'
def add_favorite_link(link):
    with open('favorites.txt', 'a') as f:
        f.write(f"{link}\n")

# Function to load favorite links
def load_favorite_links():
    if os.path.exists('favorites.txt'):
        with open('favorites.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    return []

# Function to tag a webcam link
def tag_link(link, tag):
    if tag not in tagged_links:
        tagged_links[tag] = []
    tagged_links[tag].append(link)

# Function to search links by term
def search_webcam_links(links, term):
    return [link for link in links if term.lower() in link.lower()]

# Function to open a selected webcam URL in a new tab
def open_webcam_link(link, time_to_close=None):
    logging.info(f"Opening {link} in a new browser tab...")
    webbrowser.open_new_tab(link)
    log_visited_link(link)

    if time_to_close:
        time.sleep(time_to_close)
        print(f"Closing link after {time_to_close} seconds...")  # Placeholder for actual close functionality

# Function to display the list of webcam URLs
def display_webcam_links(links):
    if not links:
        print("\nNo webcam feeds available.")
        return
    print("\nAvailable Webcam Feeds:")
    for idx, link in enumerate(links, 1):
        print(f"{idx}. {link}")

# Function to show help information for each command
def show_help():
    print("""
    Available Commands:
    - list: Displays the available webcam links.
    - open <number> [time]: Opens the webcam link at the specified number. Optionally, set time (in seconds) to auto-close the tab.
    - search <term>: Searches for links containing the specified term.
    - favorites: Shows your favorite webcam feeds.
    - fav <number>: Adds the link at the specified number to favorites.
    - visited: Displays links you have visited.
    - quick add <shortcut> <number>: Adds a shortcut for quick access to a webcam link.
    - quick <shortcut>: Opens the webcam link assigned to the shortcut.
    - tag <number> <tag>: Tags a webcam link for later filtering.
    - filter tag <tag>: Filters and displays links with the specified tag.
    - random: Opens a random webcam link.
    - history: Displays the history of visited links with timestamps.
    - exit: Exits the viewer.

    Usage:
    - Use the command 'open' followed by the number of the link, e.g., 'open 1' to open the first link.
    - To quickly search links, use 'search <term>'.
    """)

# Main function to interact with the user via CLI
def run_webcam_viewer():
    # Check for help argument
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        show_help()
        return

    # Ask user to select directory or use root
    directory = input("Enter directory to load webcam links from (leave blank for root): ").strip()
    if not directory:
        directory = '.'

    links = load_webcam_links(directory)
    current_links = links  # Track the current list to display and open

    if not links:
        logging.error("No webcam links to display.")
        return

    while True:
        print("\nCommands: 'list', 'open <number> [time]', 'search <term>', 'favorites', 'remove <number>', 'fav <number>', 'visited', 'quick add <shortcut> <number>', 'quick <shortcut>', 'tag <number> <tag>', 'filter tag <tag>', 'random', 'history', 'exit'")
        command = input("Enter a command: ").strip().lower()

        if command == 'list':
            current_links = links
            display_webcam_links(current_links)

        elif command.startswith('open'):
            # Open the specified webcam link, optionally with a timer
            try:
                parts = command.split()
                index = int(parts[1]) - 1
                time_to_close = int(parts[2]) if len(parts) > 2 else None

                if 0 <= index < len(current_links):
                    open_webcam_link(current_links[index], time_to_close)
                else:
                    print(f"Invalid number. Please select a number between 1 and {len(current_links)}.")
            except (IndexError, ValueError):
                print("Usage: open <number> [time_in_seconds]")

        elif command.startswith('search'):
            try:
                term = command.split(maxsplit=1)[1]
                found_links = search_webcam_links(links, term)
                if found_links:
                    current_links = found_links
                    display_webcam_links(current_links)
                else:
                    print(f"No links found containing '{term}'.")
            except IndexError:
                print("Usage: search <term>")

        elif command.startswith('quick add'):
            try:
                parts = command.split()
                shortcut = parts[2]
                index = int(parts[3]) - 1
                if 0 <= index < len(current_links):
                    quick_links[shortcut] = current_links[index]
                    print(f"Added shortcut '{shortcut}' for {current_links[index]}.")
                else:
                    print("Invalid index.")
            except IndexError:
                print("Usage: quick add <shortcut> <number>")

        elif command.startswith('quick'):
            try:
                shortcut = command.split()[1]
                if shortcut in quick_links:
                    open_webcam_link(quick_links[shortcut])
                else:
                    print(f"No quick link found for '{shortcut}'.")
            except IndexError:
                print("Usage: quick <shortcut>")

        elif command.startswith('tag'):
            try:
                parts = command.split()
                index = int(parts[1]) - 1
                tag = parts[2]

                if 0 <= index < len(current_links):
                    tag_link(current_links[index], tag)
                    print(f"Tagged {current_links[index]} with '{tag}'.")
                else:
                    print("Invalid number.")
            except (IndexError, ValueError):
                print("Usage: tag <number> <tag>")

        elif command.startswith('filter tag'):
            try:
                tag = command.split()[2]
                filtered_links = tagged_links.get(tag, [])
                current_links = filtered_links if filtered_links else links
                display_webcam_links(current_links)
            except IndexError:
                print("Usage: filter tag <tag>")

        elif command == 'random':
            if current_links:
                open_webcam_link(random.choice(current_links))
            else:
                print("No webcam links to choose from.")

        elif command == 'favorites':
            favorite_links = load_favorite_links()
            if favorite_links:
                display_webcam_links(favorite_links)
            else:
                print("No favorite webcam feeds found.")

        elif command.startswith('fav'):
            try:
                index = int(command.split()[1]) - 1
                if 0 <= index < len(current_links):
                    add_favorite_link(current_links[index])
                    print(f"Added {current_links[index]} to favorites.")
                else:
                    print("Invalid number.")
            except (IndexError, ValueError):
                print("Usage: fav <number>")

        elif command == 'visited':
            visited_links = load_visited_links()
            if visited_links:
                display_webcam_links(visited_links)
            else:
                print("No visited links found.")

        elif command == 'history':
            visited_links = load_visited_links()
            print("\nVisited Links:")
            for entry in visited_links:
                print(entry)

        elif command == 'exit':
            print("Exiting the viewer...")
            break

        else:
            print(f"Unknown command: {command}")

# Start the script
if __name__ == "__main__":
    run_webcam_viewer()
