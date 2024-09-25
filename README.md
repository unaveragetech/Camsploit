# Cam-Hackers README

## Overview

This Python script, **Insecam_camsplot.py**, is designed to scrape publicly accessible IP camera URLs from the Insecam website based on a specified country code. The collected IP addresses are saved to a text file for later use. The script utilizes the `requests` library for making HTTP requests and `re` for regular expression matching.

## Directory Structure

```
camsploit/
└── Insecam_camsplot.py
```

## Requirements

- **Python 3.x**
- Required libraries:
  - `requests`
  - `colorama`

You can install the required libraries using pip:

```bash
pip install requests colorama
```

## How to Use

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/AngelSecurityTeam/Cam-Hackers.git
   cd camsploit
   ```

2. **Run the Script**:
   Execute the script from your terminal:
   ```bash
   python Insecam_camsplot.py
   ```

3. **Input Country Code**:
   The script will display a list of countries along with their codes. When prompted, enter the two-digit country code (e.g., `US` for the United States).

4. **Output**:
   The script will save the found IP addresses to a file named `{country}.txt` (e.g., `US.txt`).

## Code Explanation

### Imports and Initialization

- **Imports**: The script imports necessary modules for HTTP requests, regular expressions, terminal color formatting, and random number generation.
- **Colorama**: Initializes Colorama for colored terminal output.

### Setting Up Headers

Headers are set up to mimic a web browser request to prevent potential blocking by the server:

```python
headers = CaseInsensitiveDict()
headers["Accept"] = ...
headers["User-Agent"] = ...
```

### Fetching Country Data

The script makes a GET request to Insecam to retrieve a list of countries and their associated codes:

```python
resp = requests.get(url, headers=headers)
data = resp.json()
countries = data['countries']
```

### Displaying Country Codes

A colored ASCII art header is printed, followed by a list of countries and their codes:

```python
for key, value in countries.items():
    print(f'Code : ({key}) - {value["country"]} / ({value["count"]})')
```

### Fetching IP Camera URLs

1. **User Input**: Prompts the user to enter a country code.
2. **Retrieve Camera Data**: The script fetches pages of IP camera data for the specified country.
3. **Regular Expression Matching**: It uses regex to find camera URLs within the HTML response.
4. **Saving Results**: IP addresses are saved to a file, and each is printed in the terminal.

### Error Handling

The script includes a try-except block to handle potential errors during requests or file operations. If an error occurs, it will simply skip to the final print statement.

## Note

This script is intended for educational purposes only. Use responsibly and ensure compliance with applicable laws and ethical standards regarding privacy and data access.

## Disclaimer

The authors do not endorse any illegal activities associated with the use of this script. Always respect privacy and legal boundaries.

Here's a revised version of your instruction set for clarity and readability:

---

### Instructions to Run the Script

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```

2. **Load the Repository in a Codespace**:
   Navigate to the cloned repository in your Codespace.

3. **Install Required Packages**:
   Run the following command to install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**:
   Execute the script with:
   ```bash
   python Insecam_camsplot.py
   ```

### Expected Output

The script will display a list of country codes and their corresponding country names, for example:
```
   (                             (             )  
   )\      )     )               )\     (   ( /(  
 (((_)  ( /(    (     (   `  )  ((_) (  )\  )\()) 
 )\___  )(_))   )\  ' )\  /(/(   _   )\((_)(_))/  
((/ __|((_)_  _((_)) ((_)((_)_\ | | ((_)(_)| |_   
 | (__ / _` || '  \()(_-<| '_ \)| |/ _ \| ||  _|  
  \___|\__,_||_|_|_| /__/| .__/ |_|\___/|_| \__|  
                         
   Infinidev Team 
Code : (US) - United States / (968)
Code : (JP) - Japan / (508)
```

5. **Input a Country Code**:
   When prompted, type in the country code (e.g., `US` for the United States) to retrieve a list of camera links:
   ```
   Code(##): US
   http://119.11.196.42:86
   http://36.66.133.249:80
   ...
   ```

6. **Output File**:
   The script will save the camera links to a file named `<country_code>.txt`:
   ```
   Save File: US.txt
   ```

---
