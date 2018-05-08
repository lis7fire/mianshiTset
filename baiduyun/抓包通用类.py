#!/usr/bin/python3
# coding: utf-8
# 上面两句注释必须要，防止无法打印中文的

import datetime
import os
import re
from pyquery import PyQuery as pq
import pymysql.cursors
import requests
import algorithm
import json
import traceback
# import urllib,urllib2,re,json
# 来源url：https://pan.baidu.com/disk/home?#list/vmode=list&path=/极客学院-视频2016/极客学院(知识体系图 实战路径图)/知识体系图

HEAD_COOKIE="AD_RS_COOKIE=20080918; _trs_uv=jfddwpho_6_3g41; _trs_ua_s_1=jfddwpho_6_5vm9"
HEAD_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
HEAD_ACCEPT_ENCODING = "gzip, deflate, sdch, br"
HEAD_ACCEPT_LANGUAGE = "zh-CN,zh;q=0.8"
HEAD_CONNECTION = "keep-alive"
HEAD_REFERER = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html"
HEAD_USER_AGENT = "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 "
# HEAD_X_Requested_With = "XMLHttpRequest"


req_head = {'Accept': HEAD_ACCEPT, 'Accept-Encoding': HEAD_ACCEPT_ENCODING, 'Accept-Language': HEAD_ACCEPT_LANGUAGE,
            'Cookie': HEAD_COOKIE, 
            'Referer': HEAD_REFERER, 'User-Agent': HEAD_USER_AGENT
            }

# print(req_head)
print('--------------------')
# print("请求头: ", r.request.headers)
# print("响应头: ", r.headers)
print('--------------------')



LINK='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'
CLASS_LEVEL=['.provincetr','.citytr','.countytr','.towntr','.villagetr']
def zhuaqu(htmlurl,level,is_connect_web=True):
    if not is_connect_web:
        home_res=('d76e889b6aafd3087ac3bd56f4d4053a','3fce7b5a87d8238bc7619ea3f592b5695dde7e3c','1515054506')
        print('home_page的调试模式！！！')
        return home_res
        pass
    global LINK,req_head
    print(LINK+htmlurl)
    r=requests.get(LINK+htmlurl,headers=req_head)
    r.encoding='gb2312'
    respon_text=r.text
    # print('respon_text的联网模式：',respon_text)
    doc = pq(respon_text, parser='html')
    print('--------------------')
    print('doc的联网模式：',r.encoding)
    return doc
    pass


def chaifen(items):
    proviences={}
    for item in items: # 遍历每个个股
        for i in item.items('td'):
            proviences[i.text()]={'proID':i('a').attr('href') }
    return proviences
    pass

def city(items):
    citys=[]
    for item in items: # 遍历每个个股
        print('--------citys(2):------------')
        city={'cityID':0,'cityURL':'0','cityName':'村名'}
        city['cityID']=item('td').eq(0).text()
        city['cityURL']=item('td')('a').attr('href')
        city['cityName']=item('td').eq(1).text()    
        citys.append(city)
        # for i in item.items('td'):
        #     citys[i.text()]={'proID':i('a').attr('href') }
    print('citys(2):',citys)
    return citys
    pass

def village(items):
    vills=[]
    for item in items: # 遍历每个个股
        print('--------village(1):------------')
        vill={'villID':0,'typeID':0,'villName':'村名'}
        vill['villID']=item('td').eq(0).text()
        vill['typeID']=item('td').eq(1).text()
        vill['villName']=item('td').eq(2).text()
        vills.append(vill)
    print('village(2):',vills)
    return vills

def zhengze( doc,level,debug=False):
    if debug:
        home_html='"sign1":"3fce7b5a87d8238bc7619ea3f592b5695dde7e3c","sign2": "q=0;o};",    "sign3":"d76e889b6aafd3087ac3bd56f4d4053a","timestamp":1515054506," '
        pass 
    global CLASS_LEVEL
    items = doc(CLASS_LEVEL[level]).items()
    print('zhengze(1):：',items)
    print('zhengze(2)：level：',level)
    result=[]
    if level==0:
        result=chaifen(items)
        print('level=0000000000000000000')
    if level==4:
        result=village(items)
        print('level=444444444444')
    if level==1 or level==2  or level==3 :
        print('level=22222222200')
        result=city(items)
    return result

def main():
    print('主函数：')
    proviences={}
    doc=zhuaqu('index.html',0)
    proviences=zhengze( doc,0,debug=False)
    print('--------aaaaaa------------')
    print(proviences)

    for x in proviences.keys():
        print("main(1):",proviences.get(x))
        doc=zhuaqu(proviences.get(x)['proID'],1)
        proviences.get(x)['citys']=zhengze( doc,1,debug=False)
        for city in proviences.get(x)['citys']:
            print("main(2):",city.get('cityURL'))
            doc=zhuaqu(city.get('cityURL'),2)
            city['countys']=zhengze( doc,2,debug=False)
            # proviences.get(x)['citys'][i]=city
    print("main(2):",proviences)

    filein = open('./jieguo.txt', 'w')
    print('开始读取in文件：')
    filein.write(str(proviences))
    filein.close()

        
if __name__ == '__main__':
    main()
