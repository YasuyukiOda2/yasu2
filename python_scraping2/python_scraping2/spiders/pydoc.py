# -*- coding: utf-8 -*-
import scrapy
from python_scraping2.items import TitleAndLink
from ..selenium_middlewares import close_driver
#from ..selenium_middlewares import getTitle
#from ..selenium_middlewares import getLink
#from ..selenium_middlewares import searchKeyword

class PydocSpider(scrapy.Spider):
    name = 'pydoc'
    allowed_domains = ['docs.python.jp']
    start_urls = ['https://docs.python.jp/3/index.html']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "python_scraping2.selenium_middlewares.SeleniumMiddleware": 0,
        },
        "DOWNLOAD_DELAY": 0.5,
    }

    def parse(self, response):
        item = TitleAndLink()
        title_list = []
        link_list = []
        for (title, link) in zip (response.css('ul.search a::text').extract(), response.css('ul.search a::attr("href")').extract()):
            title_list.append(title)
            link_list.append(link)            
            item['title'] = title_list
            item['link'] = link_list
        #searchKeyword()
        #item['title'] = getTitle()
        #item['link'] = getLink()
        yield item

    def closed(self, reason):
        close_driver()
