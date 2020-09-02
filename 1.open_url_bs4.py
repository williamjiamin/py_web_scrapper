from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def get_page_title(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bso=BeautifulSoup(html.read())
        title=bso.title
    except AttributeError as e:
        return None
    return title

url='https://888888zhaobudao.com/'
title=get_page_title(url)

if title==None:
    print("There is no Title in the page , Oh No!!!")
else:
    print(title)



