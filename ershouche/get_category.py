# !/usr/bin/env/python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf8")
url = 'http://cs.58.com/'

# def get_category(url):
#     # 得到58同城所有的分类url。
#     html = requests.get(url)
#     source = etree.HTML(html.text)
#     urls = source.xpath('//ul[@class="icoNav"]/li/a/@href')
#     urls[0] = 'http://cs.58.com' + urls[0]
#     for url in urls:
#         print url
#     return urls

def get_list(first_url):
    basic_url = 'http://cs.58.com'
    fin_url = []
    html = requests.get(first_url)
    context =etree.HTML(html.text)
    url_list = context.xpath('//ul[@class="clearfix"]/li/a/@href')
    for url in url_list:
        fin_url.append(basic_url+url)
    # print fin_url
    return fin_url

def make_sure(projects):
    """
    first_page.py
    处理传递进来的数据项
    :param projects: xpath选择的list对象
    :return: 清理完成的对象  str
    """
    if projects:
        projects = projects[0]
    else:
        projects = None
    return projects

url = 'http://cs.58.com/ershouche/'
get_list(url)