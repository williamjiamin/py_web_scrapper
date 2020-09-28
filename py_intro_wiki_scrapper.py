import time
import urllib

import requests
from bs4 import BeautifulSoup

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found it, Yeah!!!!!!")
        return False
    elif len(search_history) > max_steps:
        print("It is a loooooooooop!!!!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("OMG! .Maybe we can not find it . I am going to play my ps5!")
        return False
    else:
        return True

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    content_div = soup.find(id='mw-content-text').find(class_='mw-parser-output')

    name_link = None

    for element in content_div.find_all('p', recursive=False):
        if element.find('a', recursive=False):
            name_link = element.find('a', recursive=False).get('href')
            break

    if not name_link:
        return

    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', name_link)

    return first_link


crawl_log = [start_url]

while crawl(crawl_log, target_url):
    print (crawl_log[-1])

    first_link = find_first_link(crawl_log[-1])
    if not first_link:
        print('There is no first link here. I am going home')

    crawl_log.append(first_link)

    time.sleep(0.1)
