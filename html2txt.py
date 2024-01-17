# Version 1.2
# SSL verification bypassed, requests.get(url, verify=False)

import pandas as pd
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# Path to your CSV file
csv_file_path = 'websites_june_2023.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# List of websites to scrape
websites = df['Primary Source'].tolist()

# Function to fetch and parse website content
def fetch_website_content(url):
    try:
        # First try with SSL verification enabled
        response = requests.get(url, verify=True)
    except requests.exceptions.SSLError:
        try:
            # If SSL verification fails, try without verification
            response = requests.get(url, verify=False)
            print("SSL verification failed")
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"
    
    except requests.exceptions.ConnectionError:
        return f"Error: Unable to connect to {url}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()

    else:
        return f"Error: Unable to fetch content from {url} with status code {response.status_code}"
        
# Process each website
for idx, site in enumerate(websites, start=1):
    content = fetch_website_content(site)
    with open(f"Website_{idx}", 'w', encoding='utf-8') as file:
        file.write(content)