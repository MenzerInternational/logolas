import urllib.request
from bs4 import BeautifulSoup

class McScraper:
    def __init__(self, site):
        self.site = site

    def __scrape(self):
        r = urllib.request.urlopen(self.site)    # Makes a request to a site. Stores Response
        html = r.read() #Returns the HTML from the Response object. All HTML is in 'html'
        return BeautifulSoup(html, features="html.parser") # Parses the HTML in 'html'
    def find_icon(self):
        sp = self.__scrape()


McScraper('https://nytimes.com').find_icon()
