from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

def html_parsing(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))

html_parsing('http://data.pr4e.org/page1.htm')