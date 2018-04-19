# !/usr/bin/env/python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
from get_category import make_sure,get_list
import re
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import pymongo

conn = pymongo.MongoClient(host='localhost', )
db = conn.tongcheng
hello = db.ershouche_regular3

zong_url = 'http://cs.58.com'

def get_cars(url):
    """
    eg:    'http://cs.58.com/ershouche/pn0/'
    :param url: 当前页面的url
    :return: 返回所有车子的集合
    """
    # text =  open('text.html','r')
    # text = text.read()
    html = requests.get(url)
    source = etree.HTML(html.text)
    cars = source.xpath('//ul[@class="car_list ac_container"]/li')
    # next_page 下一个页面的url
    # next_page = source.xpath('//a[@class="next"]/@href')[0]
    next_page = source.xpath('//a[@class="next"]/@href')
    if next_page:
        next_page = next_page[0]
        next_page_url = zong_url + str(next_page)
        print next_page_url
        return cars, next_page_url
    else:
        # print 'Done!'
        return cars
    # next_page_url = zong_url + str(next_page)
    # print next_page_url
    # return cars,next_page_url

def get_car(cars):
    """
    :         cars = get_car(url)
    :param cars: 从get_cars传来的cars集合
    """
    for car in cars:
        car_url   = car.xpath('./div[@class="col col1"]/a/@href')
        car_pic   = car.xpath('./div[@class="col col1"]/a/img/@src')
        car_title = car.xpath('./div[@class="col col1"]/a/img/@alt')
        car_info  = car.xpath('./div[@class="col col2"]/div[1]/span/text()')
        car_price = car.xpath('./div[@class="col col3"]/h3/text()')
        # 使用make_sure 函数来保证能取到数据  不然就返回null
        car_url   = make_sure(car_url)
        car_pic   = make_sure(car_pic)
        car_title = make_sure(car_title)
        car_price = make_sure(car_price)
        # print car_title

        # 写入数据库
        hello.insert({
            'car_url':car_url,
            'car_pic':car_pic,
            'car_title':car_title,
            'car_info':car_info,
            'car_price':car_price,
        })


def deal_next_page(basic_url):
    """
    :param basic_url: 首页url  eg:'http://cs.58.com/ershouche/pn0/'
    :return:
    """
    context = get_cars(basic_url)
    if len(context) == 2 :
        cars = context[0]
        next_pages = context[1]
        get_car(cars)
        deal_next_page(next_pages)
        # print next_pages
    else:
        print 'Done!'

    # cars,next_pages = get_cars(basic_url)
    # # print next_page
    # get_car(cars)
    # if next_pages:
    #     deal_next_page(next_pages)
    #     print next_pages
    # else :
    #     print 'Done'



def main():
    begin_url = 'http://cs.58.com/ershouche/'
    for url in get_list(begin_url):
    # url = 'http://cs.58.com/ershouche/pn70/'
        deal_next_page(url)

if __name__ == '__main__':
    main()