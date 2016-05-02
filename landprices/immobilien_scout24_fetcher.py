from landprices.fetcher import AbstractFetcher
from landprices.offer import LandOffer
import urllib.request
import re
import time

class ImmobilienScout24Fetcher(AbstractFetcher):
    base_url = 'http://www.immobilienscout24.de/wohnen/berlin,berlin/grundstueck-kaufen'
    next_pages = ',seite-'

    def fetch(self):
        for page_num in list(range(1,20)):
            url = self.base_url
            if page_num == 1:
                url += '.html'
            else:
                url = url + self.next_pages + str(page_num) + '.html'
            resource = urllib.request.urlopen(url)
            html = resource.read().decode('utf-8')

            matches = re.findall("<div class=\"grid resultlist-container\">.+?<div class=\"grid-item one-whole palm-hide\">", html, re.DOTALL)
            for match in matches:
                link = 'NA'
                id_from_immo24 = 'NA'
                title = 'NA'
                address = 'NA'
                price = 'NA'
                area = 'NA'
                title_match = re.search("<div class=\"grid-item one-whole\">\W+<a class=\"resultlist-title\" href=\"(.+)\">(.+)</a>", match)
                if title_match.group(1) is not None:
                    link = title_match.group(1)
                    link = re.sub("^//", "", link)
                    id_match = re.search("\d+/?$", link)
                    if id_match.group(1) is not None:
                        id_from_immo24 = id_match.group(1)
                if title_match.group(2) is not None:
                    title = title_match.group(2)
                address_match = re.search("<div class=\"resultlist-address\">\W+<a href=\".+\">\W+(.+)\W+</a>", match)
                if address_match.group(1) is not None:
                    address = address_match.group(1)
                price_match = re.search("<div class=\"grid-item palm-one-third lap-one-third desk-one-third\">\W+<span class=\"resultlist-value\">(.+)</span>", match)
                if price_match.group(1) is not None:
                    price = price_match.group(1)
                area_match = re.search(
                    "<div class=\"grid-item palm-one-third lap-one-third desk-one-third properties-padding\">\W+<span class=\"resultlist-value\">\W*(.+?)\W*<span>",
                    match)
                if area_match.group(1) is not None:
                    area = area_match.group(1)
                o = LandOffer(self.get_fetcher_name(), id_from_immo24, link, title, address, price, area, time.strftime("%Y-%m-%d"))
                self.results += o

    def get_fetcher_name(self):
        return 'ImmobilienScout24'
