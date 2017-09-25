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
    start_urls = ['https://docs.python.jp/3/']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "python_scraping2.selenium_middlewares.SeleniumMiddleware": 0,
        },
        "DOWNLOAD_DELAY": 0.5,
    }

    def parse(self, explain_list):
        item['explain'] = explain_list
        yield item

    def closed(self, reason):
        close_driver()
