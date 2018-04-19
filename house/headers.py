# !/usr/bin/env/python
# -*- coding:utf-8 -*-
import requests

# url = 'http://cs.58.com/chuzu/pn3/'
urls = ['http://cs.58.com/chuzu/?PGTID=0d200002-0019-e8c5-f34b-2beaa82c73ef&ClickID=1',
       'http://cs.58.com/chuzu/pn3/?PGTID=0d3090a7-0019-e037-d847-d6c1913dbc6a&ClickID=2',
        'http://cs.58.com/chuzu/pn4/?PGTID=0d3090a7-0019-eac7-5613-4fdc86cd2537&ClickID=2',]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Referer': ,
    'Cookie': ' f=n; userid360_xml=ACA07436EAA2EDDB47BB4F58923B5F89; time_create=1524840438167; id58=c5/njVq7qNISb2zSA7SI'
              'Ag==; 58tj_uuid=34647c97-851b-4611-b0b8-11aeef645241; als=0; xxzl_deviceid=ebTsDjFioNFFCL0cd0cQ58oZK'
              'YWiknZPj8GiAacXS6uXq599400E%2FAznzo4GglwU; commontopbar_myfeet_tooltip=end; wmda_uuid=5e880b2a8bd8e4'
              '14a19e46af8b14e633; wmda_new_uuid=1; __track_id=20180328223959444842393999993279250; gr_user_id=5404'
              '7abc-0a39-4bbb-a006-eacb9b033870; city=cs; 58home=cs; myfeet_tooltip=end; Hm_lvt_dcee4f66df28844222e'
              'f0479976aabf1=1522248479,1522331117; Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511=1522331167; Hm_lvt_7e5c'
              '639c8aa3025f1f9601874b225e02=1522331167; _ga=GA1.2.1785048683.1522331168; wmda_visited_projects=%3B1'
              '731916484865%3B1732038237441%3B1731918550401%3B2385390625025%3B1409632296065%3B1732030748417; common'
              'Topbar_myfeet_tooltip=end; Hm_lvt_3013163ef40dcfa5b06ea83e8a1a797f=1522338424; bdshare_firstime=1522'
              '338457357; Hm_lvt_e15962162366a86a6229038443847be7=1522338613; Hm_lvt_e2d6b2d0ec536275bb1e37b4210858'
              '03=1522338617; final_history=33265922165448%2C33508956666666%2C29304304238278%2C31682673978795%2C326'
              '79659755313; Hm_lvt_d32bebe8de17afd6738ef3ad3ffa4be3=1522248001,1522338318,1522419363,1522497746; XQ'
              'H=%7B%22w%22%3A%5B%7B%22id%22%3A%22857465%22%2C%22t%22%3A1523372991401%7D%5D%7D; Hm_lvt_ae019ebe1942'
              '12c4486d09f377276a77=1523372992; __utma=253535702.1785048683.1522331168.1522338425.1523372992.2; __u'
              'tmz=253535702.1523372992.2.2.utmcsr=cs.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/chuzu/; comm'
              'ontopbar_new_city_info=414%7C%E9%95%BF%E6%B2%99%7Ccs; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1522330'
              '747,1523495449; Hm_lvt_4d4cdf6bc3c5cb0d6306c928369fe42f=1523250456,1523339751,1523463107,1523542493; '
              'GA_GTID=0d2021ff-0019-e383-6fe5-0ab60b1ce268; _gid=GA1.2.1332832644.1523542523; new_uv=22; utm_source'
              '=; spm=; new_session=0; wmda_session_id_2385390625025=1523544793446-535ea780-2683-dcab; wmda_session_i'
              'd_1731916484865=1523545489756-446cff32-58c6-5896; firstLogin=true; Hm_lvt_a3013634de7e7a5d307653e15a0'
              '584cf=1523545507; init_refer=https%253A%252F%252Fgraph.qq.com%252Foauth2.0%252Fshow%253Fwhich%253DLogi'
              'n%2526display%253Dpc%2526autoLogin%253D0%2526response_type%253Dcode%2526client_id%253D200065%2526scope'
              '%253Dget_user_info%252Cget_qq_level%252Cget_info%252Clist_album%252Cget_fanslist%2526state%253DNqkCHmK'
              'zUcTzI4jtDAv7FnYdxAhUsBtf%2526redirect_uri%253Dhttps%25253A%25252F%25252Fpassport.58.com%25252Fthd%252'
              '52Foauthlogin%25252Fpc%25252Fqzone%25253Fpath%25253Dhttps%2525253A%2525252F%2525252Fjianli.58.com%2525'
              '252Fresumedetail%2525252Fsingles%2525252F3_neraTEOs_edvnvZp_ErNlEDkTE6pTeyXnvPknpsvTA5fTedYnGtfMGyXnhs'
              'unErsnE0knemQTEH*%2525253FiuType%2525253Dp_0%25252526PGTID%2525253D0d303691-0019-eeea-825a-7b249b32153'
              '0%25252526ClickID%2525253D1%25252526pts%2525253D1523545553702%252526source%25253Dpassport; ppStore_fin'
              'gerprint=AD1497E01D29D71C7F3083D3B5F2DFB90B8868F6E1792490%EF%BC%BF1523545562638; f=n'


}
proxy = {
    # 'http': 'http://218.72.109.241:18118',
    'https': 'https://60.177.230.68:18118',
}
s = requests.session()
s.keep_alive = False
for url in urls:
    html = requests.get(url,headers=headers)
    print html.text
    print len(html.text)