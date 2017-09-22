import os.path
from urllib.parse import urlparse
from scrapy.http import HtmlResponse
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.keys import Keys
import time
from python_scraping2.utils import get_url, getExampleSentence

driver = PhantomJS()
words = ['for', 'print']
HEADS = ['F', 'P']

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        driver.get(request.url)
        driver.find_element_by_link_text('総索引').click()
        for (H, w) in zip(HEADS, words):
            driver.find_element_by_link_text(H).click()
            url_now = driver.current_url
            url_list = get_url(url_now, w) #utils.get_url
            getExampleSentence(request, url_list, w) #utils.getExampleSentence

        input_element.send_keys('for')
        input_element.send_keys(Keys.ENTER)
        time.sleep(5)
        return HtmlResponse(driver.current_url,
            body = driver.page_source,
            encoding = 'utf-8',
            request = request)


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



body > div.document > div.documentwrapper > div > div > table > tbody > tr > td:nth-child(2) > dl > dd:nth-child(48) > dl > dt > a:nth-child(1)
