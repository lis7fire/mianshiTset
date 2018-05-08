#!/usr/bin/python3
# coding: utf-8
# 上面两句注释必须要，防止无法打印中文的

import datetime
import os
from pyquery import PyQuery as pq
import pymysql.cursors
import requests
# import urllib,urllib2,re,json

ids=[]
names=[]
personids=[]
filein=open('txts/jieguo.txt','r')
print('开始读取in文件：')
while 1:
	temp=filein.readline()
	if temp:
		# print temp
		ls=temp.split('|');
		ids.append(ls[0].decode('utf-8'))#仪utf8编码来读取txt的内容【txt是以utf8编码保存的】
		print( ls[1])
		names.append(ls[1].decode('utf-8'))
		personids.append(ls[2])
	else:
		break;
filein.close()

print( ids)
print(names)
print(personids)

for x in xrange(len(personids)):
    fileout=open('txts/out.txt','a',5);
    # fileout.write(ids[x].encode('utf-8').strip().lstrip()+',')
    # fileout.write(names[x].encode('utf-8').strip().lstrip()+',')
    fileout.write(personids[x].encode('utf-8').strip().lstrip()+',')

    # print fileout.read(1)
    fileout.close()
    pass

URL = 'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/'+date_of_today
head = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0) ',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html, application/xhtml+xml, */*', 'Cookie': ''}
r = requests.get(URL, headers=head)
print('--------------------')
# print("响应头", r.headers)
# print("请求头", r.request.headers)
print(r.text,"utf-8")