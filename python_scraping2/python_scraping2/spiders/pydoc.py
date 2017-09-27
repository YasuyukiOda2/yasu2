# -*- coding: utf-8 -*-
import scrapy
import copy
from python_scraping2.items import getExplain
from python_scraping2.utils import get_url, getExplainSentence, getExplainList
from ..selenium_middlewares import golLinkListPage, backIndex, close_driver
#from urllib.parse import urljoin

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

    def parse(self, response):
        response1 = copy.deepcopy(response)
        start_url = 'https://docs.python.jp/3/'
        words = ['for', 'print']
        HEADS = ['F', 'P']
        example_sentence_list = []
        explain_list = []
        example_sentence_list = []
        #print('wordsは{}、initials_linkは{}'.format(words, response.url))
        for (H, w) in zip(HEADS, words):
            url_linklistpage = golLinkListPage(H)
            #print(url_linklistpage)
            assert url_linklistpage != None, "miss url_linklistpage"
            w_url_list = get_url(url_linklistpage, w) #utils.get_url
            print('ぐぎぎぎぐがが')
            print(w_url_list)
            assert w_url_list != None or len(w_url_list) > 0, "miss w_url_list"
            example_sentence_list = getExplainSentence(
                example_sentence_list, start_url, w_url_list, w) #utils.getExplainSentence
            #print(example_sentence_list)
            assert len(example_sentence_list) > 0, "miss example_sentence_list"
            explain_list_add = getExplainList(words, example_sentence_list) #utils.getExplainList
            #print(explain_list_add)
            assert explain_list_add != None, "miss explain_list_add"
            for e in explain_list_add:
                explain_list.append(e)
            index_page = backIndex(response)
            example_sentence_list = []
            #print(w_url_list)
            #w_url_list2 = w_url_list
            w_url_list = []
        #print("今確認したいのは{}".format(explain_list))
        #for e in explain_list:
        #    print(e)

        item = getExplain()
        item['explain'] = explain_list
        #print(w_url_list2)
        yield item

    def closed(self, reason):
        close_driver()
