import os.path
from urllib.parse import urlparse
from scrapy.http import HtmlResponse
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.keys import Keys
import time
from python_scraping2.utils import get_url, getExampleSentence, getExplainList

driver = PhantomJS()
words = ['for', 'print']
HEADS = ['F', 'P']
explain_list = []

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        request1 = request
        driver.get(request.url)
        driver.find_element_by_link_text('総索引').click()
        explain_list = []
        for (H, w) in zip(HEADS, words):
            driver.find_element_by_link_text(H).click()
            url_now = driver.current_url
            url_list = get_url(url_now, w) #utils.get_url
            example_sentense_list = getExampleSentence(request1, url_list, w) #utils.getExampleSentence
            explain_list = getExplainList(words, example_sentense_list, explain_list) #utils.getExplainList
        return explain_list

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

def close_driver():
    driver.close()
