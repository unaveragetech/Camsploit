# Camsploit

## Overview

**Camsploit** is a Python-based tool that scrapes publicly accessible IP camera URLs from the Insecam website, allowing users to explore cameras from around the world based on a specified country code. The script provides an interactive way to view these camera streams, navigate through them, and save links for later use. Users can organize saved camera feeds into custom directories.

This tool is for educational purposes only and should be used responsibly in compliance with all applicable laws regarding privacy and data access.

## Features

- **Scrape IP Camera Feeds**: Fetch public camera links from Insecam based on country codes.
- **Interactive Viewer**: Browse through camera feeds in your browser with "next" and "back" navigation.
- **Save and Organize Links**: Save camera feed links into user-specified folders for future access.
- **Terminal-Based Navigation**: Easily view, browse, and organize camera streams via the terminal.

## Directory Structure

```
camsploit/
├── Insecam_camsplot.py  # Core scraping logic
└── viewer.py            # Interactive camera feed viewer
```

## Requirements

- **Python 3.x**
- Required libraries:
  - `requests`
  - `colorama`
  - `webbrowser` (part of Python standard library)

Install the required libraries with:

```bash
pip install -r requirements.txt
```

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/AngelSecurityTeam/Camsploit.git
cd camsploit
```

### 2. Install Dependencies

Run the following command to install necessary Python packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Scraping Script

The core script, `Insecam_camsplot.py`, fetches camera feeds from Insecam based on the country code you provide. To run the script:

```bash
python Insecam_camsplot.py
```

### 4. Input Country Code

After running the script, a list of country codes will be displayed. Enter the code corresponding to the country you want to scrape (e.g., `US` for the United States).

```bash
Code(##): US
```

The script will then scrape and display a list of IP camera URLs for that country and save them to a file named `<country_code>.txt` (e.g., `US.txt`).

### 5. Viewing and Managing Camera Feeds

Once the links are scraped, use the `viewer.py` script to interactively view, browse, and manage the camera feeds:

```bash
python viewer.py
```

- **Navigation**: Use `n` for next, `b` for back, and `q` to quit.
- **View in Browser**: The selected camera feed will open in your default web browser.
- **Saving Links**: Save specific camera links into a directory of your choice.

### 6. Example Output

After entering the country code, the tool will begin fetching IP camera links like so:

```
Fetching camera data for the United States...
http://119.11.196.42:86
http://36.66.133.249:80
http://36.68.150.219:8082
...
Save File: US.txt
```

When using `viewer.py`:

```
Current link (1/10): http://119.11.196.42:86
Opening http://119.11.196.42:86 in web browser...
Enter 'n' for next, 'b' for back, 's' to save, 'q' to quit: n
```

## Code Explanation

### `Insecam_camsplot.py`

This script handles scraping IP camera URLs from Insecam:
- **HTTP Requests**: Uses the `requests` library to fetch pages from Insecam.
- **Country Codes**: Retrieves a list of country codes and their camera counts, displaying them for the user to choose from.
- **Regex Matching**: Extracts camera URLs using regular expressions.
- **File Output**: Saves camera URLs into a file named `<country_code>.txt`.

### `viewer.py`

This script provides interactive functionality to view and manage the camera feeds:
- **Browser Viewing**: Opens the camera feed in your default web browser.
- **Navigation**: Browse through the links interactively.
- **Saving**: Save the selected camera feed URL into a custom directory with a user-defined name.

## Example Directory Structure

After running the scripts, your directory might look like this:

```
camsploit/
├── Insecam_camsplot.py
├── viewer.py
├── US.txt                # Saved camera links from the United States
└── saved_links/          # Directory created by the user to save specific links
```

## Notes and Disclaimer

- This tool is intended for educational purposes only. Ensure you are following all applicable legal and ethical guidelines regarding privacy and the use of publicly accessible data.
- The authors of **Camsploit** are not responsible for any misuse of this tool. Always respect privacy, and use the script responsibly.

## License

[Include any license information here if applicable.]

---

Let me know if you need any adjustments!
