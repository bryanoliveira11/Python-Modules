# web scraping
import re

import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333'
response = requests.get(url)
raw_html = response.content
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

if parsed_html.title is not None:
    print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one(
    '#intro > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > h2:nth-child(1)')

if top_jobs_heading is not None:
    # print(top_jobs_heading.text)
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
