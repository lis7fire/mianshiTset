	#!/usr/bin/python  
#-*-coding:utf-8-*- 
# 上面两句注释必须要，防止无法打印中文的
import urllib,urllib2,re,json,sys
reload(sys)
sys.setdefaultencoding('utf8')

question='{"id":"402880a951579cfb015157b773d80f6b","answer":"这个事"}'#字典类型
print  "111"
print type(question)# reauest_question.read();#encode('iso8859-1')
print  "2222222"
print str(question)
aaa=json.dumps(question,ensure_ascii=False)#字典类型
print  "3333333333333"
print  type(aaa)
print  "4444443"
print str(aaa)
print aaa.strip().lstrip();
print  "3333333333333"

data='{"attributes":null,"obj":[{"id":"402880a951579cfb015157a508200b7b","tmms":"公务员执行公务时，认为上级的决定或者命令有错误的，可以向上级提出改正或者撤销该决定或者命令的意见；上级不改变该决定或者命令，或者要求立即执行的，公务员( )。","rigthAnswers":"A","choicesList":[{"content":"不应当执行该决定或者命令","id":"402880a951579cfb015157a5086c0b7d","nexttm":"","total":0,"input":"0","tmid":"402880a951579cfb015157a508200b7b","orders":0},],"th":501,"tmlx":"only"},],"success":true,"msg":"操作成功"}'
data='{"obj":[{"id":"402880a951579cfb015157a508200b7b","tmms":"公务员执行公务时，认为即执行的，公务员( )。","rigthAnswers":"A","th":501,"tmlx":"only"},],"msg":"操作成功"}'
b='{"id":"402880a951579cfb015157a508200b7b","tmms":"公务员执行公务时，认为即执行的，公务员( )。","rigthAnswers":"A","th":501,"tmlx":"only"}'

jsondata=''#json.loads(data)#字典类型
print  "3333333333333"
print  type(jsondata)
print  "4444443"

print str(jsondata)
print  "3333333333333"
b=b.encode("gbk",'ignore')#用来对str类型【utf8编码】转码成为gbk
question=eval(b)#将字符串转化为字典
# tt=question.decode("gbk")
print question
tm=question['tmms']
# print tm.decode("gbk")
temp=tm.decode("gbk")
print 'sasasssssssss'
print  temp
print  type(temp)
a='正确'
b='abcd'
print len(a)
print type(a)
print len(b)

c=temp.encode('utf-8')

a=str(question)

print a.encode('utf-8')
print unicode(a,"utf-8")
print  type(a)

tem='{"attributes":null,"obj":null,"success":true,"msg":"操作成功"}'
# tem=tem.replace('"','\'')
# tem=tem.decode("utf-8")
print type(tem)
ansresp=json.loads(tem)
print ansresp['success']
if not ansresp['success']:
	print '答题失败了,结束！'
	# break;
else:
	print "答题成功了："
pass

