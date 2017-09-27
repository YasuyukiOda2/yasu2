import os.path
import time
import copy
import requests
from urllib.parse import urlparse
from scrapy.http import HtmlResponse
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.keys import Keys
from python_scraping2.utils import get_url, getExplainSentence, getExplainList
#from python_scraping2.items import getExplain

driver = PhantomJS()
words = ['for', 'print']
HEADS = ['F', 'P']

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        #url_list = []
        #explain_list = []
        #example_sentence_list = []
        request1 = copy.deepcopy(request)
        driver.get(request1.url)
        driver.find_element_by_link_text('総索引').click()
        r = requests.get(driver.current_url)
        r.encoding = r.apparent_encoding
        return HtmlResponse(driver.current_url,
            body = driver.page_source,
            encoding = r.encoding,
            request = request)

        #for (H, w) in zip(HEADS, words):
            #driver.find_element_by_link_text(H).click()
            #url_now = driver.current_url
            #url_list = get_url(url_now, w) #utils.get_url
            #assert type(url_list) != 'NoneType', "url_list = NoneType object"
            #assert len(url_list) > 1, "url_list couldn't get"
            #print('確認')
            #print(type(example_sentence_list)) # 確認用
            #example_sentence_list = getExplainSentence(
            #    example_sentence_list, request1, url_list, w) #utils.getExplainSentence
            #explain_list_add = getExplainList(words, example_sentence_list) #utils.getExplainList
            #for e in explain_list_add:
            #    explain_list.append(e)
            #driver.get(request1.url)
            #driver.find_element_by_link_text('総索引').click()
            #example_sentence_list = []
        #print(explain_list)
        #print(driver.page_source)
        #print(type(driver.page_source))
        #return HtmlResponse(driver.current_url,
            #body = explain_list,
            #encoding = 'utf-8',
            #request = request)

#def searchKeyword():
#    input_element = driver.find_element_by_name('q')
#    input_element.send_keys('for')
#    input_element.send_keys(Keys.ENTER)

#def getTitle():
#    input_element = driver.find_element_by_name('q')
#    input_element.send_keys('for')
#    input_element.send_keys(Keys.ENTER)
#    assert '検索' in driver.title
#    return driver.find_element_by_css_selector('#search-results > ul > li:nth-child(1) > a').text

#def getLink():
#    input_element = driver.find_element_by_name('q')
#    input_element.send_keys('for')
#    input_element.send_keys(Keys.ENTER)
#    return driver.find_element_by_css_selector('#search-results > ul > li:nth-child(1) > a').get_attribute("href")

def golLinkListPage(HEAD):
    driver.find_element_by_link_text(HEAD).click()
    url_now = driver.current_url
    return url_now

def backIndex(response1):
    driver.get(response1.url)
    r = requests.get(driver.current_url)
    r.encoding = r.apparent_encoding
    #print('ぐぎぎぎぐがが')
    #print(response1.url)
    #driver.find_element_by_link_text('総索引').click()
    #driver.get('https://docs.python.jp/3/genindex.html')
    #return HtmlResponse(driver.current_url,
    #    body = driver.page_source,
    #    encoding = 'utf-8')

def close_driver():
    driver.close()
