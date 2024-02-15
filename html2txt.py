# Version 1.3
# This version uses headers to bypass http request verification

# SSL verification bypassed, requests.get(url, verify=False)
import pandas as pd
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# Path to your CSV file
# csv_file_path = 'websites_june_2023.csv'

def html2txt(csv_file_path, scraped_sites_path):

    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # List of websites to scrape
    websites = df[df.columns[0]].tolist()

    for idx, site in enumerate(websites, start=1):
        content = fetch_website_content(site)
        with open(f"{scraped_sites_path}/Website_{idx}.txt", 'w', encoding='utf-8') as file:
            file.write(content)

# Function to fetch and parse website content
def fetch_website_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        # First try with SSL verification enabled
        response = requests.get(url, headers=headers, verify=True)
    except requests.exceptions.SSLError:
        try:
            # If SSL verification fails, try without verification
            response = requests.get(url, headers=headers, verify=False)
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
    elif response.status_code == 403:
        return f"Error: Access to {url} is forbidden (status code 403)"
    else:
        return f"Error: Unable to fetch content from {url} with status code {response.status_code}"
        
# Process each website
""" for idx, site in enumerate(websites, start=1):
    content = fetch_website_content(site)
    with open(f"scraped_sites/Website_{idx}.txt", 'w', encoding='utf-8') as file:
        file.write(content) """