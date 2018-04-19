# !/usr/bin/env/python
# -*- coding:utf-8 -*-

import requests
from lxml import etree

def get_lists(url):
    html = requests.get(url)
    source = etree.HTML(html.text)
    lists = source.xpath('')