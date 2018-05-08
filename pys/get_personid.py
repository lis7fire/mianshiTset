#!/usr/bin/python  
#-*-coding:utf-8-*- 
# 上面两句注释必须要，防止无法打印中文的
import urllib,urllib2,re,json

def request_get(url):
	req=urllib2.Request(url)
	resp=urllib2.urlopen(req)
	# html=resp.read()
	return  resp;

def urllib2_reuest(url,useragent,cookies):
	# reauest_lib2=urllib2.Request(url,'',headers);
	# resp=urllib2.urlopen(reauest_lib2)
	reauest_lib2=urllib2.Request(url);
	reauest_lib2.add_header('User-Agent',useragent)
	reauest_lib2.add_header('Cookie',cookies)
	resp=urllib2.urlopen(reauest_lib2)
	# html=resp.read()
	return resp;

name=r'张玮'
idcard=r"410402199103275691"
index='http://12333.andfans.cn/ansWjPcController.do?goRegisterPage&hdId=402880a946db5f390146dc0b51080002'
loginurl1=r"http://12333.andfans.cn/ansWjPcController.do?checkPersonForCard&wjId=402880a946db5f390146dc0b51080002&sldcode=419900&";# &
personpage='''http://12333.andfans.cn/ansWjPcController.do?goPersonInfoPage'''
# getgoodsurl='''http://12333.andfans.cn/ansWjPcController.do?goExchageGoodsPage&personId="+data.obj'''

useragent=' Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0';

ids=[]
names=[]
personids=[]
banknames=[]
filein=open('txts/in.txt','r')
print  '开始读取in文件：'
while 1:
	temp=filein.readline()
	if temp:
		# print temp
		ls=temp.split('|');
		ids.append(ls[0].decode('utf-8'))#仪utf8编码来读取txt的内容【txt是以utf8编码保存的】
		names.append(ls[1])
	else:
		break;
filein.close()
print names[0]

for i in xrange(len(ids)):#开始循环发包抓取发奖银行
    name=names[i].strip().lstrip()#后面是去掉字符串前后空格和特殊字符的，去掉字符串中间的空格用.replace(' ', '')
    idcard=ids[i].encode('utf-8').strip().lstrip()
    print names[i]
    
    # name=names[25].strip().lstrip()#后面是去掉空格和特殊字符的
    # idcard=ids[25].encode('utf-8').strip().lstrip()
    loginurl2='name=%s&idcard=%s' % (urllib.quote(name),idcard)#urllib.quote(name)对中文转换为gbk编码，编码后是符合url编码的
    loginurl=loginurl1+loginurl2
    
    print loginurl
    duijiang=r"http://12333.andfans.cn/ansWjPcController.do?goCheckPersonInfo&idcard=%s&wjId=402880a946db5f390146dc0b51080002" % idcard
    
    # header1={'User-Agent':useragent}
    index_resp=urllib2_reuest(index,useragent,'');
    head=index_resp.info();
    
    # 查找字符串里面的；分号
    weizhi1= head['Set-Cookie'].index(',',0);
    weizhi2= head['Set-Cookie'].index(';',20);#从字符串的第【20】个字符开始查找需要的字符，并且返回第一个的位置；
    # print head['Set-Cookie'][0:20];#取字符串的第【0-n】个字符组成的字符串；
    
    cookies=head['Set-Cookie'][0:19]+head['Set-Cookie'][weizhi1+1:weizhi2];#组装完成的cookies
    print cookies;
    
    # headers={'User-Agent':useragent,'Cookie':cookies}
    reauest_login=urllib2_reuest(loginurl,useragent,cookies);#登陆的请求包，用来登陆到服务器
    reauest_duijiang=urllib2_reuest(duijiang,useragent,cookies);#获取personId和<span>中国农业银行奖品列表</span>
    duijiang=reauest_duijiang.read();
    
    loginresp=json.load(reauest_login)
    print reauest_login.read()
    
    print loginresp['success']
    
    if loginresp['success']:
    	print "成功了："
    else:
    	print '失败了'
    	personids.append('i');
    	banknames.append('i');
    	continue;
    
    print "开始："
    print loginurl1+loginurl2;
    # print reauest_login.read();
    # print request_get(index).read();#h获取此页面的返回头里面的set-cookies；其余不需要
    print '''-------------------------*---''';
    # 下面是搜索兑奖返回页面的personid和银行信息的
    person=re.findall(r'personId = "[\w]+"',duijiang);#正则搜索personid
    personid=person[0].split('"');#删除没用的字符
    bank=re.findall(r'<div class="c-title"><span>[^\w]+</span>',duijiang)#正则搜索发奖银行
    bankname=bank[0].split('>');#删除没用的字符
    
    print  'personid是：'+person[0];
    print  'personid是：'+personid[1];
    personids.append(personid[1]);
    print  '领奖银行是：'+bank[0];
    print  '领奖银行是：'+bankname[2];
    banknames.append(bankname[2])
    print i

for x in xrange(len(personids)):
    fileout=open('txts/out.txt','a',5);
    fileout.write(ids[x].encode('utf-8').strip().lstrip()+'|'+names[x].strip().lstrip()+'|'+personids[x]+'|'+banknames[x]+'\n')
    # print fileout.read(1)
    fileout.close()
    pass
