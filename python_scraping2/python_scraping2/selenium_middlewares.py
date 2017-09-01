import os.path
from urllib.parse import urlparse
from scrapy.http import HtmlResponse
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.keys import Keys
import time

driver = PhantomJS()

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        driver.get(request.url)
        input_element = driver.find_element_by_name('q')
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
