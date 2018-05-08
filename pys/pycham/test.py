#!/usr/bin/python3
# coding: utf-8
# 上面两句注释必须要，防止无法打印中文的

import sys
from lxml import etree
import requests

URL = 'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2017-12-11/'
head = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0) ',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html, application/xhtml+xml, */*', 'Cookie': ''}

r = requests.get(URL, headers=head)
print('--------------------')
print("响应头", r.headers)
print("请求头", r.request.headers)
print('--------------------')
# print(r.text)
print('--------------------')
tree = etree.HTML(r.text)
print(tree.xpath('/html/body/div[3]/div[2]/div[1]/string(.)'))

# 输入多组数据并输出
for line in sys.stdin:
    for value in line.split('连续输入：'):
        print(value)
