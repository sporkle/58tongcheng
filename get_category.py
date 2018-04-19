# !/usr/bin/env/python
# -*- coding:utf-8 -*-

import requests
from lxml import etree

def get_category(url):
    # 得到58同城所有的分类url。
    html = requests.get(url)
    source = etree.HTML(html.text)
    urls = source.xpath('//ul[@class="icoNav"]/li/a/@href')
    urls[0] = 'http://cs.58.com' + urls[0]
    for url in urls:
        print url
    return urls

if __name__ == '__main__':
    url = 'http://cs.58.com/'
    get_category(url)