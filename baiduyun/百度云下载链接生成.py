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

'''
COOKIE中变动的字段：
BDCLND=91Mz4PuAQqrrr%2B0plTyxqHNK2v7XDzmPDglcIEQt9uI%3D;
MCITY=-%3A; 
Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1514801279,1514801523,1514807401,1514811465;
PANPSC=298461236142715097%3Acvzr9Jxhf5DlI0a0yYJfmCOAoXNFwReXsg0gWUDJHkjXG9GmBZpeFcD%2BGm5EjO5jLPY%2BF1C2z9fxTJ3v1z1m%2BnR1lPHAQEb1l29mtrQhjoN%2BSJWX9%2F9F%2FCC9yOinRwwiKg6bXhEDmDblx9uR5zc7VkTo8K6GUSXPWZS%2FCparmSwCDm3pOf6hqyxKPKTDDqOPAg5t6Tn%2BoatGYDbXt8Y3lw%3D%3D;
'''
errno = ''
VERSION = "1.0.1"

HEAD_COOKIE_BDCLND = 'BDCLND=jTANjfZMNtr32HwuKTmoS7FDzPgQG2OnnvyTbwyLOkw=;'
HEAD_COOKIE_MCITY = 'MCITY=-131:;'
HEAD_COOKIE_Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0 = 'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1514385494,1514386300,1514647712,1514647867;'
HEAD_COOKIE_PANPSC = 'PANPSC=13679979192454137669:ZjFd1PuLJ+CynWRlA/AGiaikII2LTYQX49AGnxnjY+dKu8WyLCLL4eXStNSa0XHHC63U2dDStAqhcX9Lqc6TJ9cb0aYFml4VWVlWJGg7qeZ9c6xaO4oLgT0Imr6lK+/C+JWDNkK4hUt7m6T14kJ2T2NtiaXV6jA2rsgnNL+LYct9tn9thbnTpv7IiW4JizVaiS3u8yDNz5M=;'

HEAD_COOKIE_STATIC = "\
yundetect_httpport=10001;\
bdshare_firstime=1441637184814;\
panlogin_animate_showed=1;\
BAIDUID=9E282C0C20251223D9067410870BB3D7:FG=1;\
PSTM=1500106635;\
BIDUPSID=B72858A392123BF808B2AC361C077180;\
__cfduid=d0f761a353ea4d050004e39c134a521641503915605;\
BDUSS=UtJY2RlR1JYWFNjeXVvZlJ-Sms1aEl6R1BCODRNeGF6Z0RENE5wNTA4fmt-TmhaSVFBQUFBJCQAAAAAAAAAAAEAAABBkQQMejM5MzUyMTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAORvsVnkb7FZO;\
PANWEB=1;\
STOKEN=5a7573d529f685ffec8d3a553fecc952d3e6d2a47e623dc89eac1415f63d36d3;\
SCRC=bc2972c1a8266b9ad3cb9f220f4a897f;\
PSINO=1;\
H_PS_PSSID=1454_21119_18560_17001_25227_25436_25178;\
BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;\
Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1514652578;\
"
# HEAD_COOKIE = HEAD_COOKIE_STATIC + HEAD_COOKIE_BDCLND + HEAD_COOKIE_MCITY + HEAD_COOKIE_Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0 + HEAD_COOKIE_PANPSC


HEAD_ACCEPT = "application/json, text/javascript, */*; q=0.01"
HEAD_ACCEPT_ENCODING = "gzip, deflate, sdch, br"
HEAD_ACCEPT_LANGUAGE = "zh-CN,zh;q=0.8"
HEAD_CONNECTION = "keep-alive"
HEAD_HOST = "pan.baidu.com"
HEAD_REFERER = "https://pan.baidu.com/disk/home?"
HEAD_USER_AGENT = "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 "
HEAD_X_Requested_With = "XMLHttpRequest"


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as cookfile:
        ck = json.load(cookfile)
    return ck


def write_json(filename, dict_info):
    with open(filename, 'w', encoding='utf-8') as wfile:
        wfile.write(json.dumps(dict_info))
    return ck

ck =read_json('./cook.json') 
HEAD_COOKIE = ck['cookie_baidu']
COOKIE_TIME=ck['cookie_timestamp']

req_head = {'Accept': HEAD_ACCEPT, 'Accept-Encoding': HEAD_ACCEPT_ENCODING, 'Accept-Language': HEAD_ACCEPT_LANGUAGE,
            'Cookie': HEAD_COOKIE, 'Host': HEAD_HOST,
            'Referer': HEAD_REFERER, 'User-Agent': HEAD_USER_AGENT, 'X-Requested-With': HEAD_X_Requested_With
            }
'''
==:%3D%3D
[:%5B
]:%5D
'''
down_link_static_PARS2 = '''\
&type=dlink\
&ct=pcygj\
&cv=5.6.3.4\
&channel=chunlei\
&web=1\
&app_id=250528\
&bdstoken=1ed63c7f24fd368f96f7073bd49b89ab\
&clienttype=0\
'''

'''sign=cQYtRX3fvPdf7ZYw2J34rCDfuznxe5KMPVIhP5k0sR5NVCMIr1qzMQ==&timestamp=1515054506'''

# print(req_head)
print('--------------------')
# print("请求头: ", r.request.headers)
# print("响应头: ", r.headers)
print('--------------------')


def zhengze(home_html, debug=False):
    '''[正则匹配获取sign1和sign3，以便计算sign2的值]

    [description]

    Arguments:
        home_html {[str]} -- [网盘主页的html]

    Keyword Arguments:
        debug {bool} -- [是否开启调试模式] (default: {False})

    Returns:
        [集合] -- [返回 sign3,sign1,timestamp时间戳]
    '''
    if debug:
        home_html = '"sign1":"3fce7b5a87d8238bc7619ea3f592b5695dde7e3c","sign2": "q=0;o};", "sign3":"d76e889b6aafd3087ac3bd56f4d4053a","timestamp":1515054506," '
        pass
    # print(home_html)
    sign1 = re.search(r'(?<=sign1":").+?(?=",)', home_html).group()
    sign3 = re.search(r'(?<=sign3":").+?(?=",)', home_html).group()
    timestamp = re.search(r'(?<=timestamp":).+?(?=,")', home_html).group()
    print(sign1)
    print(sign3)
    print(timestamp)
    return sign3, sign1, timestamp
    pass


def home_page(is_connect_web=False):
    '''[summary]

    [抓取百度网盘主页返回用正则提取的sign和时间戳]

    Keyword Arguments:
        is_connect_web {bool} -- [是否以联网模式访问] (default: {False})

    Returns:
        [type] -- [description]
    '''
    if not is_connect_web:
        cook_sign_dict = read_json('./cook.json')
        # home_res = ('cQYtRX3fvPdf7ZYw2J34rCDfuznxe5KMPVIhP5k0sR5NVCMIr1qzMQ==', '1515054506')
        home_res = (cook_sign_dict['sign'], cook_sign_dict['sign_timestamp'])
        print('home_page的调试模式！！！')
        return home_res
        pass
    link = 'https://pan.baidu.com/disk/home?'
    global req_head, HEAD_COOKIE,COOKIE_TIME
    respon_text = requests.get(link, headers=req_head).text
    home_res_tmp = zhengze(respon_text)
    print('home_page的联网模式：', home_res_tmp)
    sign = algorithm.base64_baidu(algorithm.sign2(home_res_tmp[0], home_res_tmp[1]))
    wjson_data = {"cookie_baidu": HEAD_COOKIE,
                  "cookie_timestamp": COOKIE_TIME,
                  "sign_timestamp": home_res_tmp[2],
                  "sign": sign,
                  "sign1": home_res_tmp[1],
                  "sign3": home_res_tmp[0]
                  }
    write_json('./cook.json', wjson_data)
    print('保存sign成功！')
    return sign, home_res_tmp[2]  # 因为写入文件了，返回值没有用了


def initlink(sign, timestamp, fidlist):
    '''[生成download的链接]

    [主要是生成sign签名]

    Arguments:
        sign3 {[type]} -- [description]
        sign1 {[type]} -- [description]
        timestamp {[type]} -- [description]
        fidlist {[str]} -- [要下载的文件的fid，一次下载多个的话就是一个list]

    Returns:
        [str] -- [获取下载链接的url]
    '''
    global down_link_static_PARS2
    sign = sign.replace('/', '%2F')
    sign = sign.replace('+', '%2B')
    sign = sign.replace('=', '%3D')
    fidlist = '%5B' + fidlist + '%5D'
    logid = 'MTUxNDY1Mjg3MTY5NzAuNzY4OTg5NjY3ODcwMzY5OA=='
    down_link_pars1 = 'sign=' + sign + '&timestamp=' + timestamp + '&fidlist=' + fidlist + '&logid=' + logid
    # print(down_link_pars1) #下载的文件名：02、Cocos2d-x游戏开发.rar
    link = 'https://pan.baidu.com/api/download?' + down_link_pars1 + down_link_static_PARS2
    return link
    pass


def download_page(sign, timestamp, fidlist='236514448554701', is_connect_web=True):
    '''[summary]

    [构造下载页面请求包并且获取最终包含下载链接的响应包]

    Arguments:
        home_res {[set]} -- [包含sign3 sign1 times]

    Keyword Arguments:
        is_connect_web {bool} -- [description] (default: {True})

    Returns:
        [dict] -- [包含下载连接的响应结果]
    '''
    if not is_connect_web:
        r_json = '{"errno":0,"request_id":84267772485035342,"dlink":[{"fs_id":"916188959762109","dlink":"https:\/\/d.pcs.baidu.com\/file\/6b4f39cc4a791ed4700c171a6977cf4a?fid=2433224667-250528-916188959762109&time=1515049922&rt=pr&sign=FDTAERVC-DCb740ccc5511e5e8fedcff06b081203-nTg1faUlM6qrNwYzneQPSZopDR8%3D&expires=8h&chkv=1&chkbd=1&chkpc=&dp-logid=84267772485035342&dp-callid=0&r=794357218"}]}'
        # r_json='{"errno":-6,"request_id":84159854721116628}'
        return json.loads(r_json)
        pass
    sig = initlink(sign, timestamp, fidlist)
    print('download_page函数联网模式，Download页面的Link：\n', sig)
    global req_head
    r_json = requests.get(sig, headers=req_head).text
    js = json.loads(r_json)
    return js


def init_errno():
    '''
    [从json文件中获取错误码和对应的错误类型，初始化全局字典errno]

    '''
    global errno
    errno = read_json('./canshu.json')
    # print(type(errno))


def final_url(js):
    '''[summary]

    [从最后的响应包中提取最终可以用来迅雷下载的url]

    Arguments:
        js {[dict]} -- [download_page页面的响应包]
    '''
    print('-------')
    init_errno()
    if js["errno"] == 0:
        print('真实链接获取成功！文件 {} 的下载链接是：\n {}\n'.format(js['dlink'][0]['fs_id'], js['dlink'][0]['dlink']), )
        pass
    else:
        print('真实链接获取失败！请求id为：{},失败编号：{},错误类型：{} '.format(js['request_id'], js['errno'], errno[str(js['errno'])]))


tmp_dirs = {}  # 缓存当前文件夹下的文件列表
cur_path, father_path, up_path = '/', '/', '/'  # 当前目录，父目录，上次操作的目录


def list_page(dir='/'):
    '''[summary]

    [获取当前目录下的文件列表和元数据，并且打印出来]

    Keyword Arguments:
        dir {str} -- [当前目录] (default: {'/'})
    '''
    global cur_path, father_path, up_path, tmp_dirs
    link = 'https://pan.baidu.com/api/list?dir={}&bdstoken=1ed63c7f24fd368f96f7073bd49b89ab&logid=&num=100&order=name&desc=0&clienttype=0&showempty=0&web=1&page=1&channel=chunlei&web=1&app_id=250528'.format(
        dir)
    # print('list链接为：\n', link)
    print('--------------------')
    r = requests.get(link, headers=req_head)
    filelist = json.loads(r.text)
    # print(filelist)
    if filelist['errno'] == 0:
        tmp_paths = dir.split('/')
        if dir == '/' or len(tmp_paths) == 2:
            father_path = '/'
            print('当前目录是根目录!!! ')
        else:
            father_path = dir.rstrip(dir.split('/')[-1])
            father_path = father_path.rstrip('/')
        up_path = cur_path
        cur_path = dir
        tmp_dirs = {}
        i = 1
        print('当前目录：{} ，上一层目录：{} , 上次操作目录：{}'.format(cur_path, father_path, up_path))
        for x in filelist['list']:
            print('{} : {} | {} fid：{}'.format(i, x['path'], {1: '文件夹', 0: '文件'}[x['isdir']], x['fs_id']))
            tmp_dirs[i] = x  # ['path']
            i += 1
            pass
    else:
        print('请求id为：{},失败编号：{},错误类型：{} '.format(filelist['request_id'], filelist['errno'],
                                                 errno[str(filelist['errno'])]))
        pass


def main():
    print('主函数：')
    home_res = home_page(is_connect_web=False)
    js = download_page(home_res[0], home_res[1], is_connect_web=True)
    final_url(js)
    list_page()

    global father_path, tmp_dirs
    while True:
        user_input = input('请输入编号：')
        if user_input == '..':
            list_page(father_path)
        else:
            try:
                user_input = int(user_input)
            except Exception as e:
                print('必须输入一个数字！！！现在退出程序！')
                traceback.print_exc()
                return
            else:
                print(tmp_dirs)
                list_page(tmp_dirs[user_input]['path'])


if __name__ == '__main__':
    main()
