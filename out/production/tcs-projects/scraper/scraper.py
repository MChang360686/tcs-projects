#!/usr/bin/env python3

# https://stackoverflow.com/questions/11783875/importerror-no-module-named-bs4-beautifulsoup
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = input("Please enter a URL to scrape")

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all image tags (img) on the webpage
images = soup.find_all('img')

# Extract and print the src attribute of each image
for img in images:
    src = img.get('src')
    print(src)
