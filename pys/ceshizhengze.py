
#-*-coding:utf-8-*- 
# 上面两句注释必须要，防止无法打印中文的
import urllib,urllib2,re,json,sys,codecs

print  'qweq：'

filein=open('33.html','r').read()
print  '开始读取in文件：'
# try:  
# 	temp=filein.readlines()
# finally:  
#     filein.close()

print type(filein)


# a='<divclass="content">女:你多大？<br/>男:22<br/>女:没问你年龄！<br/>男:我也回答的不是年龄啊。<!--1456399077--></div><divclass="stats"><spanclass="stats-vote"><iclass="number">767</i>好笑</span><spanclass="stats-comments"><spanclass="dash">·</span>'
# filein=filein.replace(' ', '')
filein=filein.replace('\n', '')
print filein

result=re.findall(r'<div class="content">(.*?)</div>',filein)
# result=re.findall(r'<divclass="content">.+--></div>',filein)#正则搜索发奖银行

print result
print type(result)
print len(result)
for x in xrange(0,len(result)):
	print result[x]
	print '\n'
	pass
