# !/usr/bin/env/python
# -*- coding:utf-8 -*-

import requests
from lxml import etree

def get_category(url):
    html = requests.get(url)
    source = etree.HTML(html.text)
    urls = source.xpath('//ul[@class="ym-mainmnu"]/li/span[1]/a/@href')
    names = source.xpath('//ul[@class="ym-mainmnu"]/li/span[1]/a/text()')
    for url,name in zip(urls,names):
        print name + " : " + 'http://cs.58.com' + url + ''

url = 'http://cs.58.com/sale.shtml?PGTID=0d100000-0019-e32d-f795-dcbc65aa0ab8&ClickID=2'
get_category(url)