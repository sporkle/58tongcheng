# !/usr/bin/env/python
# -*- encoding:utf-8 -*-

import requests
from lxml import etree
from functions import *
import time

import pymongo

conn = pymongo.MongoClient(host='localhost', )
db = conn.tongcheng
chuzu = db.house_chuzu
ershoufang = db.hopuse_ershou1


def get_category(first_url):
    """
    得到所有的分类  共三类
    :param first_url:  house 的最初url
    :return:           分类的url
    """
    source       = get_html_context(first_url)
    category_url = source.xpath('//a[@class="ui-all-btn"]/@href')
    return category_url

def get_context_one(page_url):
    """
    category_urls[0]解析
    从当前页面得到 包含的所有的contexts
    :param page_url:                    从get_category 中得到的第一个url  其它的由页面解析的next_page得到
    :return:  houses,next_page          当前页面的所有contests
    """
    houses = []
    context_source   = get_html_context(page_url)
    print page_url
    contexts         = context_source.xpath('//ul[@class="listUl"]/li')
    next_page_before = context_source.xpath('//a[@class="next"]/@href')
    for context in contexts:
        """图片地址  house连接  house标题 房间数 单价"""
        # image = context.xpath('./div[@class="img_list"]/a/@href')
        url   = context.xpath('./div[@class="des"]/h2/a/@href')
        title = context.xpath('./div[@class="des"]/h2/a/text()')
        room  = context.xpath('./div[@class="des"]/p[1]/text()')
        place = context.xpath('./div[@class="des"]/p[2]/a/text()')
        price =  context.xpath('./div[@class="listliright"]/div[2]/b/text()')

        # image = make_sure(image)
        url   = make_sure(url)
        title = make_sure(title)
        room  = make_sure(room)
        price = make_sure(price)
        # print price
        one_house = {
            'url':url,
            'place':place,
            'title':title,
            'room':room,
            'price':price
            }
        houses.append(one_house)
    next_page = make_sure(next_page_before)
    # print contexts
    return houses,next_page

def get_context_two(page_url):
    """
    category_urls[1:2]的页面解析
    :param page_url:            要解析的页面的url
    :return:  contexts          当前页面的所有contests
    """
    context_source = get_html_context(page_url)
    print page_url
    contexts         = context_source.xpath('//ul[@class="house-list-wrap"]/li')
    next_page_before = context_source.xpath('//a[@class="next"]/@href')
    next_page        = make_sure(next_page_before)
    houses = []
    for context in contexts:
        image = context.xpath('./div[@class="pic"]/a/@href')
        url   = context.xpath('./div[@class="list-info"]/h2/a/@href')
        title = context.xpath('./div[@class="list-info"]/h2/a/text()')
        room  = context.xpath('./div[@class="list-info"]/p[1]/span/text()')
        # room 中含有多个信息
        place = context.xpath('./div[@class="list-info"]/p[2]/span[1]/a/text()')
        detail_place = context.xpath('./div[@class="list-info"]/p[2]/span[2]/text()')
        jjr_info     = context.xpath('./div[@class="list-info"]/div[@class="jjrinfo"]/text()')
        total_price  = context.xpath('./div[@class="price"]/p[1]/b/text()')
        avg_price    = context.xpath('./div[@class="price"]/p[2]/text()')
        # print "hello"

        image   = make_sure(image)
        url     = make_sure(url)
        title   = make_sure(title)
        detail_place = make_sure(detail_place)
        jjr_info = make_sure(jjr_info)
        total_price = make_sure(total_price)
        avg_price = make_sure(avg_price)
        black = ''
        for item in room:
            room = black + item
        for item in place:
            place = black + item

        house = {'iamge':image,'url':url, 'title':title, 'detail_place':detail_place, 'jjr_info':jjr_info,
                 'totle_price':total_price, 'avg_price': avg_price, 'room':room , 'place': place}
        houses.append(house)

    return houses, next_page


def into_db(houses):
    if (len(houses[0]) < 8):
        for one_house in houses:
            chuzu.insert(one_house)
    else:
        for one_house in houses:
            ershoufang.insert(one_house)

def del_next_page(context_funz, next_page_url, url_suffix):
    # time.sleep(1)
    next_page_url = next_page_url + url_suffix
    contexts,next_page = context_funz(next_page_url)
    into_db(contexts)
    if next_page:
        del_next_page(context_funz,next_page,url_suffix)
    else:
        print "Done"

def main():
    url = 'http://cs.58.com/house.shtml'
    category_urls = get_category(url)
    # for url in category_urls:
    """
    house的3个 category 中后两个的规则是不一样的
    """
    # url = category_urls[0]
    # url_suffix = [
    #     '?PGTID=0d3090a7-0019-e883-ff10-607bbfc6df41&ClickID=2',
    #     '?PGTID=0d200001-0019-e1f7-9be7-2b9489cce32e&ClickID=1',
    #     '?PGTID=0d200001-0019-e35b-a5f9-171ede616b84&ClickID=1',
    #     '?PGTID=0d200001-008d-2fb3-389c-a93705ad5a34&ClickID=2',
    # ]
    # kinds = get_sub_category(url)
    # for url,url_suffix in zip(kinds,url_suffix):
    #     url = url + '?PGTID=0d100000-0019-eee9-271b-44552c93d560&ClickID=2'
    #     houses,next_page = get_context_one(url)
    #     into_db(houses)
    #     if next_page:
    #         del_next_page(get_context_one, next_page, url_suffix)

    for secend_url in category_urls[1:2]:
        secend_url = secend_url + '?PGTID=0d100000-0019-ed6f-446a-86c32e6bf044&ClickID=2'
        houses,next_page = get_context_two(secend_url)
        into_db(houses)
        url_suffix = '?PGTID=0d200001-0019-e35b-a5f9-171ede616b84&ClickID=1'
        if next_page:
            del_next_page(get_context_two, next_page,url_suffix)


if __name__ == '__main__':
    main()