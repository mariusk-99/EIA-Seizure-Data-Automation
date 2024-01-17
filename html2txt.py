# Version 1.1
# SSL verification fails requests.get(url, verify=True)

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
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    else:
        return "Error: Unable to fetch content from " + url

# # Create instance of FPDF class
# pdf = FPDF()
# pdf.set_font("Arial", size=12)

# Process each website
for idx, site in enumerate(websites, start=1):
    content = fetch_website_content(site)
    with open(f"Website_{idx}", 'w', encoding='utf-8') as file:
        file.write(content)