import requests
import json
from bs4 import BeautifulSoup

url="https://www.w3schools.com/html/html_tables.asp"
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
page_title = soup.title.text if soup.title else "No Title Found"
print(page_title)


for link in soup.find_all('a'):
    href=link.get('href')
    print(href)

tabledata=[]
table=soup.find("table")
if table:
    rows=table.find_all('tr')
    for row in rows:
        cols=row.find_all('td')
        row_data=[col.text.strip() for col in cols]
        print(row_data)

extracted_data={
    "page_title":page_title,
    "total_links":len(href),
    "table_data":row_data,
}
with open('extractdata.json', 'w',encoding="utf-8") as file:
    json.dump(extracted_data, file, indent=4)
print("saved")

