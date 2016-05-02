from urllib.error import HTTPError

from landprices.fetcher import AbstractFetcher
from landprices.offer import LandOffer
import urllib.request
import re
import time

class ImmobilienScout24Fetcher(AbstractFetcher):
    base_url = 'http://www.immobilienscout24.de/wohnen/berlin,berlin/grundstueck-kaufen'
    next_pages = ',seite-'

    def fetch(self):

        for page_num in list(range(1, 50)):
            url = self.base_url
            if page_num == 1:
                url += '.html'
            else:
                url = url + self.next_pages + str(page_num) + '.html'
            try:
                resource = urllib.request.urlopen(url)
                print(url)
                html = resource.read().decode('utf-8')
                if re.match("Die Seite konnte leider nicht aufgerufen werden", html, re.IGNORECASE):
                    break

                matches = re.findall("<div class=\"grid resultlist-container\">.+?<div class=\"grid-item one-whole palm-hide\">", html, re.DOTALL)
                for match in matches:
                    link = 'NA'
                    id_from_immo24 = 'NA'
                    title = 'NA'
                    address = 'NA'
                    price = 'NA'
                    area = 'NA'
                    title_match = re.search("<div class=\"grid-item one-whole\">\W+<a class=\"resultlist-title\" href=\"(.+)\">(.+)</a>", match)
                    if title_match:
                        link = title_match.group(1)
                        link = re.sub("^//", "", link)
                        id_match = re.search("www.immobilienscout24.de/expose/(\d+)", link)
                        if id_match:
                             id_from_immo24 = id_match.group(1)
                    if title_match:
                        title = title_match.group(2)
                    address_match = re.search("<div class=\"resultlist-address\">\W+<a href=\".+\">\W+(.+)\W+</a>", match)
                    if address_match:
                        address = address_match.group(1)
                    price_match = re.search("<div class=\"grid-item palm-one-third lap-one-third desk-one-third\">\W+<span class=\"resultlist-value\">(.+)</span>", match)
                    if price_match:
                        price = price_match.group(1)
                    area_match = re.search(
                        "<div class=\"grid-item palm-one-third lap-one-third desk-one-third properties-padding\">\W+<span class=\"resultlist-value\">\W*(.+?)\W*<span>",
                        match)
                    if area_match:
                        area = area_match.group(1)
                    o = LandOffer(self.get_fetcher_name(), id_from_immo24, link, title, address, price, area, time.strftime("%Y-%m-%d"))
                    self.results.append(o)
            except HTTPError:
                # On page not found error we exit the for loop. It means we retrieved enough pages for today.
                # This error most likely will show up in other cases, for the time being we break out of the loop.
                break

    def get_fetcher_name(self):
        return 'ImmobilienScout24'
