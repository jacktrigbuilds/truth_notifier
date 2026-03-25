import feedparser
from bs4 import BeautifulSoup
# import requests

# site = requests.get('https://truthsocial.com/@realDonaldTrump')
data = feedparser.parse('https://trumpstruth.org/feed ')
soup = BeautifulSoup(data.entries[0].description, 'lxml')
print(soup.get_text())
# soup_direct = BeautifulSoup(site.content, 'html.parser')
#(soup_direct.prettify())

