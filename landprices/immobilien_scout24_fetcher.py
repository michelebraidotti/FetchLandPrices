from landprices.fetcher import AbstractFetcher
from landprices.offer import LandOffer
import urllib.request
import re

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
            print('==============>' + url)
            resource = urllib.request.urlopen(url)
            html = resource.read().decode('utf-8')

            matches = re.findall("<div class=\"grid resultlist-container\">.+?<div class=\"grid-item one-whole palm-hide\">", html, re.DOTALL)
            #matches = re.findall("<div class=\"grid resultlist-container\">", html)
            for match in matches:
                title_match = re.search("<div class=\"grid-item one-whole\">\W+<a class=\"resultlist-title\" href=\"(.+)\">(.+)</a>", match)
                link = title_match.group(1)
                link = re.sub("^//", "", link)
                title = title_match.group(2)

                print('************************')
                print(link)
                print(title)

                address_match = re.search("<div class=\"resultlist-address\">\W+<a href=\".+\">\W+(.+)\W+</a>", match)
                address = address_match.group(1)
                price_match = re.search("<div class=\"grid-item palm-one-third lap-one-third desk-one-third\">\W+<span class=\"resultlist-value\">(.+)</span>", match)
                price = price_match.group(1)
                area_match = re.search(
                    "<div class=\"grid-item palm-one-third lap-one-third desk-one-third properties-padding\">\W+<span class=\"resultlist-value\">\W*(.+?)\W*<span>",
                    match)
                area = area_match.group(1)


                print(address)
                print(price)
                print(area)
                print('************************')

            #o = LandOffer(self.get_fetcher_name(), "Buch", "1 buck", "30/4/2016")
            #self.results.append(o)
            #o1 = LandOffer(self.get_fetcher_name(), "Zepernick", "3 bucks", "30/4/2016")
            #self.results.append(o1)

    def get_fetcher_name(self):
        return 'ImmobilienScout24'
