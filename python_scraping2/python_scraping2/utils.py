import logging
import lxml.html
import readability
import requests
import re
from urllib.parse.urljoin

# ReadabilityのDEBUG/INFOレベルのログを表示しないようにする
logging.getLogger('readability.readability').setLevel(logging.WARNING)

def get_url(url, word):
    """
    キーワードに関する記述のあるurlを取得
    """

    # 空白・改行を除く本文を取得
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    text = r.text.strip()

    # 正規表現でリンクを抽出
    pattern1 = "<dt>\s*" + word + "\s*<dt/>"
    pattern1_1 = pattern1 + "\s*<dd><dl>\s*<dt>(.*)\s*</dt>"
    if re.search(pattern1_1, text).group(1):
        text1_1 = re.search(pattern1_1, text).group(1)
        pattern1_1_1 = '<a href="([^"]*)">'
        url_iterater = re.finditer(pattern1_1_1, text1_1)
        url_list = []
        for match_url in url_iterater:
            url_list.append(match_url.group(1))
        return url_list

def getExplain(request, url_list, w):
    for url in url_list:
        url = urljoin(request, url)
