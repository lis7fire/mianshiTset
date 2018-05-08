#!/usr/bin/python  
#-*-coding:utf-8-*- 
# 上面两句注释必须要，防止无法打印中文的

import re
text='''’‘''var bankId = "402880a95141b3d5015141bfaf5e0003";
					var personId = "8ae07e0252af62740152b9d2a6f118a4";
					var destUrl = "goodsController.do?exchangeGoods&goodsId="+goodsId+"&bankId="+bankId+"&personId="+personId+"&symbol=pc";
					window.location.href=destUrl;'''
ht=ur'''			<div class="c-title"><span>中国银行奖品列表</span></div>
			<table width="96%" border="1">
			  <tbody><tr>
			  '''

# pp=re.findall(r'personId = "[\w]+"',text)
p1=re.findall(r'<div class="c-title"><span>[^\w]+[^<]',ht)
pp=p1[0].encode('utf-8')
print  pp

ids=[]
names=[]
filein=open('in.txt','r')
print  '开始'
while 1:
	temp=filein.readline()
	if temp:
		print temp
		ls=temp.split('|');
		ids.append(ls[0].decode('utf-8'))#仪utf8编码来读取txt的内容【txt是以utf8编码保存的】
		names.append(ls[1])
	else:
		break;
filein.close()
print  '结束'
print ids[0].encode('utf-8'),
# print names[2].encode('utf-8')



fileout=open('out.txt','a',5);
for i in xrange(len(ids)):
	fileout.write(ids[i].encode('utf-8')+'|'+names[i])
# fileout.write(ids[0].encode('utf-8'))
# fileout.write(names[2])#因为txt文本就是用utf8编码的，所以写入txt时不需要解码

fileout.close()
