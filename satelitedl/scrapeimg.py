# coding: utf-8
"""
"""
from urllib.request import urlopen
import urllib.error
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class ScrapingImg:
    """ScrapingImg.
    scraping satelite picture from "http://weather.is.kochi-u.ac.jp/sat/ALL/"
    """

    def __init__(self, url: str):
        """__init__.

        Args:
            url (str): url
        """
        self.url = url
        self.UrlParse = urlparse(self.url)
        self.html = urlopen(self.url)
        self.bsObj = BeautifulSoup(self.html, 'lxml')

    def fetch_img_url(self) -> list:
        """fetch_img_url.

        Args:

        Returns:
            list:
        """
        self.href_list = []
        self.link_list = []
        for link in self.bsObj.findAll("a"):
            href = link.attrs['href']
            if "http" not in href:
                link = self.url + href

            self.href_list.append(href)
            self.link_list.append(link)
        return self.href_list

    def download_file(self):
        """download_file.
        """
        for i in range(len(self.href_list)):
            print(self.link_list[i])
            try:
                with urlopen(self.link_list[i]) as web_file:
                    data = web_file.read()
                    with open(self.href_list[i], 'wb') as local_file:
                        local_file.write(data)
            except urllib.error.URLError as e:
                print(e)
