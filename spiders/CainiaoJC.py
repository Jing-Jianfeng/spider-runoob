# -*- coding: utf-8 -*-
import scrapy
from runoob.items import RunoobItem
from bs4 import BeautifulSoup

class CainiaojcSpider(scrapy.Spider):
    name = 'CainiaoJC'
    allowed_domains = ['www.runoob.com']
    start_urls = ['https://www.runoob.com/mongodb/mongodb-window-install.html']

    def parse(self, response):
        page=response.body
        soup = BeautifulSoup(page, "lxml")
        results = soup.find_all("a", attrs={"target": "_top"})
        for result in results:
            items=RunoobItem()
            if result.attrs["href"][0] is not "/":
                items["url"] =self.allowed_domains[0]+"/mongodb/"+ result.attrs["href"]

            else:
                items["url"] =self.allowed_domains[0]+ result.attrs["href"]
            items["title"] = result.attrs["title"]
            yield items

