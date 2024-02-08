# EIA-Seizure-Data-Automation

### This project automates the data entry in the EIA Seizure Database.

## How does it work?

1. Given a list of links, our model scrapes the given websites.
2. It then translates the text to english if the articles are in a different language
3. Then they are fed to an LLM model (gpt-3.5-turbo & gpt-4)
4. The LLM model extracts the necessary data from the text
5. The fields are then filled out and uploaded on the Seizure database
