# -*- coding:utf-8 -*-
import json
import re
import sys

from requests import get

url = "https://m.search.naver.com/p/csearch/dcontent/spellchecker.nhn"
header = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'Accept-Encoding': ', '.join(('gzip', 'deflate')),
    'Accept': '*/*',
    'Connection': 'keep-alive'
}


def getResult(s):
    return get(url, params={'q': s, '_callback': 'default'}, headers=header).text


def parseText(text):
    p = re.compile('^default\({(.*)}\);\s*$')
    html = json.loads(p.sub(r'{\1}', text))['message']['result']['html']
    return cleanHtml(html)


def cleanHtml(html):
    p = re.compile('<.*?>')
    return re.sub(p, '', html)


def check(phrase):
    return parseText(getResult(phrase))


if __name__ == "__main__":
    text = " ".join(sys.argv[1:])
    r = check(text)

    print(r)
