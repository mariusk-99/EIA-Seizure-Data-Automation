import pandas as pd
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import html2txt

# csv_file_path = "C4ADS_2023_Q1_Q2_websites.csv"
csv_file_path = "temp_url.csv"
scraped_sites_path = "scraped_sites_c4ads_2023_Q1_Q2"

html2txt.html2txt(csv_file_path, scraped_sites_path)