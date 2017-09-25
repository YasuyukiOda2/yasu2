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
    pattern2 = 
    if re.search(pattern1_1, text).group(1):
        text1_1 = re.search(pattern1_1, text).group(1)
        pattern1_1_1 = '<a href="([^"]*)">'
        url_iterater = re.finditer(pattern1_1_1, text1_1)
        url_list = []
        for match_url in url_iterater:
            url_list.append(match_url.group(1))
        return url_list

def getExplainSentence(request1, url_list, w):
    for url in url_list:
        url = urljoin(request1, url)
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        text = r.text.strip()
        example_sentense_list = getExampleSentenceList(text)
    return example_sentense_list

def getExampleSentenceList(text):
    compiled_pattern_pre = re.compile('<pre>.*?</pre>', re.DOTALL)
    example_sentence_list_html = compiled_pattern_pre.findall(text)
    example_sentense_list = excludeHTML(example_sentence_list_html)
    return example_sentense_list

def excludeHTML(example_sentence_list_html):
    pattern_html = re.compile("<[^>]*?>")
    example_sentense_list = []
    for sentence in example_sentence_list_html:
        example_sentense_list.append(pattern_html.sub("", sentence))
    return example_sentense_list

def getExplainList(words, example_sentense_list, explain_list):
    for s in example_sentence_list:
        w_list = [] # w_listを初期化
        for w in words:
            if w not in s:
                continue
            w_list.append(w)
        if len(w_list) == len(words):
            explain_list.append(s)
    return explain_list
