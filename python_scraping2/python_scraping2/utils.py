import logging
import lxml.html
import readability
import requests
import re
from urllib.parse import urljoin

# ReadabilityのDEBUG/INFOレベルのログを表示しないようにする
logging.getLogger('readability.readability').setLevel(logging.WARNING)

def get_url(url, word):

    url_list = []
    """
    キーワードに関する記述のあるurlを取得
    """

    # 空白・改行を除く本文を取得
    #print('確認')
    #print(url) #確認用
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    text = r.text.strip()
    #print(text) #確認用
    #print(word) #確認用

    # 正規表現でリンクを抽出
    pattern1 = "<dt>\s*" + word + "\s*</dt>"
    pattern1_1 = pattern1 + "\s*<dd><dl>\s*<dt>(.*)\s*</dt>"
    pattern2 = "<dt>\s*" + word + "[()].*?\s*</dt>"
    pattern2_1 = pattern2 + "\s*<dd><dl>\s*<dt>(.*)\s*</dt>"
    pattern3 = '<dt>\s<a href="(.*?)">\s*' + word + '[()].*?\s*</a>'
    pattern_list = [pattern3, pattern1_1, pattern2_1]
    for p in pattern_list:
        if re.search(p, text) and p == pattern3:
            text3 = re.search(p, text).group(1)
            url_list.append(text3)
        elif re.search(p, text) and p == pattern1_1:
            url_list_add = getUrlList(p, text)
            for u in url_list_add:
                url_list.append(u)
            #print('確認')
            #print(url_list) #確認用
            #text_href = re.search(pattern1_1, text).grop(1)
            #pattern_href = '<a href="([^"]*)">'
            #url_iterater = re.finditer(pattern_href, text_href)
            #url_list = [match_url.group(1) for match_url in url_iterater]
        elif re.search(p, text) and p == pattern2_1:
            url_list_add = getUrlList(p, text)
            for u in url_list_add:
                url_list.append(u)
            #text_href = re.search(pattern2_1, text).grop(1)
            #pattern_href = '<a href="([^"]*)">'
            #url_iterater = re.finditer(pattern_href, text_href)
            #url_list = [match_url.group(1) for match_url in url_iterater]
    #print("ajognafngjsnojnjnbjnbjng")
    #print(url_list)
    print('現在の検索単語は{}、取得したurlのリストは{}'.format(word, url_list))
    assert len(url_list) > 0, "no pattern match"
    return url_list

def getUrlList(pattern, text):
    text_href = re.search(pattern, text).group(1)
    pattern_href = '<a href="([^"]*)">'
    url_iterater = re.finditer(pattern_href, text_href)
    url_list = [match_url.group(1) for match_url in url_iterater]
    return url_list

def getExplainSentence(example_sentence_list, start_url, url_list, w):
    # print('確認')
    # print('type example_sentence_list = ' + str(type(example_sentence_list)))
    for url in url_list:
        url = urljoin(start_url, url)
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        text = r.text.strip()
        example_sentence_list_add = getExampleSentenceList(text)
        for s in example_sentence_list_add:
            example_sentence_list.append(s)
    return example_sentence_list

def getExampleSentenceList(text):
    compiled_pattern_pre = re.compile('<pre>.*?</pre>', re.DOTALL)
    example_sentence_list_html = compiled_pattern_pre.findall(text)
    example_sentence_list_add = excludeHTML(example_sentence_list_html)
    return example_sentence_list_add

def excludeHTML(example_sentence_list_html):
    pattern_html = re.compile("<[^>]*?>")
    example_sentence_list_add = [
        pattern_html.sub("", sentence) for sentence in example_sentence_list_html]
    #for sentence in example_sentence_list_html:
    #    example_sentense_list.append(pattern_html.sub("", sentence))
    return example_sentence_list_add

def getExplainList(words, example_sentence_list):
    explain_list_add = []
    for s in example_sentence_list:
        w_list = [w for w in words if w in s]
        if len(w_list) == len(words):
            explain_list_add.append(s)
    return explain_list_add
