import os
import webbrowser

# Function to automatically detect the most recent 'country.txt' file in the directory
def find_latest_ip_file():
    files = [f for f in os.listdir() if f.endswith('.txt')]
    if files:
        latest_file = max(files, key=os.path.getmtime)
        print(f"Automatically detected file: {latest_file}")
        return latest_file
    else:
        print("No '.txt' file with links found in the current directory.")
        return None

# Function to load IPs from the saved file
def load_ips(file_path):
    try:
        with open(file_path, 'r') as f:
            links = [line.strip() for line in f.readlines()]
        return links
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

# Function to navigate the links and display feeds
def navigate_links(links):
    if not links:
        print("No links to display.")
        return
    
    current_index = 0
    while True:
        current_link = links[current_index]
        print(f"\nCurrent link ({current_index+1}/{len(links)}): {current_link}")
        
        # Ask if user wants to view the feed
        view_feed = input("Do you want to view this feed? (y/n): ").strip().lower()
        if view_feed == 'y':
            open_in_browser(current_link)
        
        command = input("Enter 'n' for next, 'b' for back, 's' to save, 'q' to quit: ").strip().lower()

        if command == 'n':
            if current_index < len(links) - 1:
                current_index += 1
            else:
                print("You are at the last link.")
        elif command == 'b':
            if current_index > 0:
                current_index -= 1
            else:
                print("You are at the first link.")
        elif command == 's':
            save_link(links[current_index])
        elif command == 'q':
            break
        else:
            print("Invalid command. Try again.")

# Function to open the stream in the browser
def open_in_browser(link):
    print(f"Opening {link} in web browser...")
    webbrowser.open(link)

# Function to save the current link
def save_link(link):
    folder = input("Enter folder name to save link (leave blank for current directory): ").strip()
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    
    file_name = input("Enter the name of the file (without extension): ").strip() + ".txt"
    file_path = os.path.join(folder, file_name)

    with open(file_path, 'w') as f:
        f.write(link)
    
    print(f"Link saved to '{file_path}'.")

# Main function to run the program
def main():
    file_path = find_latest_ip_file()
    if file_path:
        links = load_ips(file_path)
        if links:
            navigate_links(links)

if __name__ == "__main__":
    main()
