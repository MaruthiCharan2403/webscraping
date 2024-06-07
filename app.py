import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
url = 'https://www.bbc.com/news'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
with open('titles.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'URL'])
    for title in soup.find_all('h2'):
        headline = title.get_text()
        headline_url = ''
        parent = title.parent
        while True:
            if parent.a:
                headline_url = parent.a['href']
                break
            parent = parent.parent
            if parent is None:
                break
        if headline_url:
            headline_url = urljoin(url, headline_url)
        writer.writerow([headline, headline_url])

print("Data scraped and saved to 'titles.csv' file.")