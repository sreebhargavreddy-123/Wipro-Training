import requests
from bs4 import BeautifulSoup
import json

# 1. URL of the webpage
URL = "https://www.w3schools.com/html/html_tables.asp"

# 2. Fetch HTML page
response = requests.get(URL)
response.raise_for_status()   # Raises error if request fails

# 3. Parse HTML with BeautifulSoup + lxml
soup = BeautifulSoup(response.text, "lxml")

# Extract Page Title
page_title = soup.title.text if soup.title else "No Title Found"

# Extract All Hyperlinks
links = []
for link in soup.find_all("a", href=True):
    links.append(link["href"])

# Extract Table Data
table_data = []

table = soup.find("table")  # first table on the page
if table:
    headers = [th.text.strip() for th in table.find_all("th")]

    for row in table.find_all("tr")[1:]:
        values = [td.text.strip() for td in row.find_all("td")]
        if values:
            table_data.append(dict(zip(headers, values)))

# Prepare JSON Data
extracted_data = {
    "page_title": page_title,
    "hyperlinks": links,
    "table_data": table_data
}

# Save to JSON File
with open("webpage_data.json", "w", encoding="utf-8") as file:
    json.dump(extracted_data, file, indent=4)

print("Data extracted and saved to webpage_data.json")
