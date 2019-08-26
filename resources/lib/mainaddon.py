import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup))
    return soup
get_soup("https://rss.art19.com/factually-with-adam-conover")

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://content.production.cdn.art19.com/images/65/f6/0d/14/65f60d14-3e56-4504-ba10-abe17c25856b/aee12f75e9cb30d31b7e0c41c2a5bc7b9bc19ab95a8e3b29b395b4d806de5a00932bd36960f7201d0142e049c55fb9933192e3b5cd8847485716e9db04814ee6.jpeg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=10):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://content.production.cdn.art19.com/images/65/f6/0d/14/65f60d14-3e56-4504-ba10-abe17c25856b/aee12f75e9cb30d31b7e0c41c2a5bc7b9bc19ab95a8e3b29b395b4d806de5a00932bd36960f7201d0142e049c55fb9933192e3b5cd8847485716e9db04814ee6.jpeg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
