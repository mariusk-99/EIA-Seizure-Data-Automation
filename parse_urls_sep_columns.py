import pandas as pd

# Manually load the file content to handle variable numbers of URLs in each cell
file_path = 'C4ADS_2023_Q1_Q2_websites.csv'

# Initialize a list to hold each line's URLs
urls_list = []

# Open the file and process each line
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Split the line by comma and strip whitespace
        urls = [url.strip() for url in line.split(',')]
        urls_list.append(urls)

# Convert the list of lists into a DataFrame where each list becomes a row
# This approach assumes the first row does not contain URLs but headers or is to be skipped
urls_df = pd.DataFrame(urls_list[1:], columns=[f'URL {i+1}' for i in range(len(max(urls_list[1:], key=len)))])

# Display the first few rows of the processed DataFrame
urls_df.head()

urls_df.to_csv("temp_url.csv", index=False)
