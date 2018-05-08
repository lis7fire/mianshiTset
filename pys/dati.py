#!/usr/bin/python  
#-*-coding:utf-8-*- 
# 上面两句注释必须要，防止无法打印中文的
import urllib,urllib2,re,json,sys

# reload(sys)
# sys.setdefaultencoding('utf8')#让系统不用ascii存储，
#@#卢川是ids[9],李梦娇ids[25]
ids=['410203198709141023','412824198912167743','410185198902040127','410223198610223526','410122198605010014','413024192310250427','413024195411060052','413024198307217017','413024198110010442','413024198210140025','413029198106140449','413001198108151516','411522199011080020','411521198901090916','413028196406050925','413028196104290958','410602197511142013','42900519860104002X','413028195903230914','413028196202130923','413028198312030930','411322198409010342','411322198207300018','413028197409017228','413026198001213040','410105201211300033','411502198703140557','413023197405080041','413025196705220024']
names=['郭珂','李琼','赵珊珊','李娜','卢川','祁素珍','胡应和','吴桂林','王娟','喻克卉','夏娟娟','张帆','杨韵秋','张健','李素梅','张传刚','桂兆伟','蔡庆','卢祥友','徐中秀','陈伟','李婧','王家祥','刘小丽','汪流永','江卓恩','韦力','许玉','梁秀枝']
personids=['8ae07e0252af62740152ee6482402fe0','8ae07e0252af62740152c69bb836594b','8ae07e0252af62740152ea75156863c5','8ae07e0252af62740152ee649c4e2fe9','8ae07e0252af62740152ee6489a12fe1','8ae07e0252af62740152eefd32bf4234','8ae07e0252af62740152eefd3ffa423c','8ae07e0252af62740152eefd4361423d','8ae07e0252af62740152eefd4479423e','8ae07e0252af62740152eefd33e54235','8ae07e0252af62740152eefd37894236','8ae07e0252af62740152eefd38c34237','8ae07e025280d5820152867d4c9a7605','8ae07e0252294f40015231148e43273d','8ae07e025280d58201528c79a0453be0','8ae07e025280d58201528c0f80ac3497','8ae07e0252352e0201525cba07ff12da','8ae07e0252294f400152298e1bcb0d4a','8ae07e0252af62740152c0d6b8e618ba','8ae07e0252af62740152c1743ef62a95','8ae07e0252af62740152c1743e000000','8ae07e0252af627401531706e0b971b1','8ae07e0252af627401531705c311718a','8ae07e0252af6274015317050c28717a','8ae07e0252af62740152c368b530343d','8ae07e0252af6274015316e31cfe6f8b','8ae07e025280d58201528d14cee950b5','8ae07e025297a00a015297a8d96a010b','8ae07e025280d58201528dc4aca77641']

# ids=['410203198709141023','412824198912167743','410185198902040127','410223198610223526','41100219900717104X','410103198705100034','410204198812032024','410223198910144520','412728199009060063','410122198605010014','413024192310250427','413024195411060052','413024198307217017','413024198110010442','413029195210020435','413024196309290040','413024198210140025','413029198106140449','413001198108151516','413029195602080429','411526198802190091','413024196309160035','413024195001180043','413024195508240025','410105198109160025','410881199005240767','410103199001290081','41108119891016906X']
# names=['郭珂','李琼','赵珊珊','李娜','任远','张博','邢婧','魏娟','李爽','卢川','祁素珍','胡应和','吴桂林','王娟','夏宗理','刘丽霞','喻克卉','夏娟娟','张帆','黄成凤','喻治珲','喻克强','王素琴','付桂芳','王婷','李梦娇','王羽羲','韩洋']
# personids=['8ae07e0252af62740152ee6482402fe0','8ae07e0252af62740152c69bb836594b','8ae07e0252af62740152ea75156863c5','8ae07e0252af62740152ee649c4e2fe9','8ae07e0252af62740152ee648fb52fe2','8ae07e0252af62740152ee6493272fe3','8ae07e0252af62740152ee6480df2fda','8ae07e0252af62740152ee647b182fd8','8ae07e0252af62740152ee647fbb2fd9','8ae07e0252af62740152ee6489a12fe1','8ae07e0252af62740152eefd32bf4234','8ae07e0252af62740152eefd3ffa423c','8ae07e0252af62740152eefd4361423d','8ae07e0252af62740152eefd4479423e','8ae07e0252af62740152eefd3b1c4239','8ae07e0252af62740152eefd3ed6423b','8ae07e0252af62740152eefd33e54235','8ae07e0252af62740152eefd37894236','8ae07e0252af62740152eefd38c34237','8ae07e0252af62740152eefd3a014238','8ae07e0252af62740152bf7ae5af7892','8ae07e0252af62740152eefd3dc0423a','8ae07e0252af62740152eefd31954233','8ae07e0252af62740152da7f97cf7255','8ae07e0252af62740152eefd4590423f','8ae07e0252af62740152ee6470dc2fd2','8ae07e0252af62740152ee64a3212ff0','8ae07e0252af62740152ee649db82fea']
# urlidcard=r'410881199005240767'#在这里写上答题人的身份证号码
# name=r'李梦娇'
num=26
while num<29:
	urlidcard=ids[num]
	name=names[num]
	# urlidcard=r'411528198905260067'#在这里写上答题人的身份证号码
	# name=r'卢静文'
	print name
	zhengque=[71,71,72,71,71]
	cuowu=[9,9,8,8,6]#cuowu值最大为11
	score=66;#设置得分,默认66分
	wrong=6;#控制总题量，总题量为：score+wrong-1；wrong值最大为11
	right=3;#控制得分，总分为64+2;最大为3，
	cishu=0;
	maxlen=3;
	useragent=' Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0';
	#402880a951579cfb015157b773d80f6b 是正确答案B 【5道错误题目，3道正确题目】
	wrongans=[{"answer":"A","id":"402880a951579cfb015157a4a2e5090b"},{"answer":"B","id":"402880a951579cfb015157a0ac5905ac"},{"id":"402880a951579cfb015157a4a6700924","answer":"A"},{"id":"402880a951579cfb015157b70ced0cfd","answer":"A"},{"id":"402880a951579cfb015157b747170e5f","answer":"C"},{"id":"402880a951579cfb015157b7682c0f2a","answer":"B"},{"id":"402880a951579cfb015157a4d2b80a33","answer":"A"},{"id":"402880a951579cfb015157b723ac0d7d","answer":"C"},{"id":"402880a951579cfb015157a4c9ae09fe","answer":"B"},{"id":"402880a951579cfb015157b728a60d9b","answer":"A"},{"id":"402880a951579cfb015157a508ba0b7f","answer":"B"}]
	rightans=[{"id":"402880a951579cfb015157b723ac0d7d","answer":"D"},{"id":"402880a951579cfb015157a4c9ae09fe","answer":"A"},{"id":"402880a951579cfb015157b728a60d9b","answer":"C"},{"id":"402880a951579cfb015157a508ba0b7f","answer":"A"}]
	
	index='http://12333.andfans.cn/ansWjPcController.do?goRegisterPage&hdId=402880a946db5f390146dc0b51080002'
	loginurl1=r"http://12333.andfans.cn/ansWjPcController.do?checkPersonForCard&wjId=402880a946db5f390146dc0b51080002&sldcode=419900&name=%s&idcard=%s" % ((urllib.quote(name),urlidcard));# &
	personpage='''http://12333.andfans.cn/ansWjPcController.do?goPersonInfoPage'''
	
	datiindex='http://12333.andfans.cn/ansWjPcController.do?goAnsTimeWjPcPage&wjId=402880a946db5f390146dc0b51080002&idcard=%s' % (urlidcard) #发包的时候，此页面无用，存放的是网页的2:00计时器
	getquestions='http://12333.andfans.cn/ansWjController.do?getChallengeQuestionList&wjId=402880a946db5f390146dc0b51080002&idcard=%s' % (urlidcard) #获取题目的页面，响应实体是json,重复发送13次即可
	answer='http://12333.andfans.cn/ansWjController.do?updateMostHeightPoint&wjId=402880a946db5f390146dc0b51080002&idcard=%s&result=' % (urlidcard) #提交答案发送的get包，result=后面跟上答案的json数据即可,返回更新后的成绩
	
	def urllib2_reuest(url,useragent,cookies):
		reauest_lib2=urllib2.Request(url);
		reauest_lib2.add_header('User-Agent',useragent)
		reauest_lib2.add_header('Cookie',cookies)
		resp=urllib2.urlopen(reauest_lib2)
		return resp;
	
	#下面是访问首页来设置cookie
	index_resp=urllib2_reuest(index,useragent,'');
	head=index_resp.info();
	# 查找字符串里面的；分号
	weizhi1= head['Set-Cookie'].index(',',0);
	weizhi2= head['Set-Cookie'].index(';',20);#从字符串的第【20】个字符开始查找需要的字符，并且返回第一个的位置；
	cookies=head['Set-Cookie'][0:19]+head['Set-Cookie'][weizhi1+1:weizhi2];#组装完成的cookies
	print cookies
	
	#下面是账号密码登陆
	reauest_login=urllib2_reuest(loginurl1,useragent,cookies);#登陆的请求包，用来登陆到服务器
	loginresp=json.load(reauest_login)
	print loginresp['success']
	if loginresp['success']:
		print "登陆成功了："
	else:
		print '登陆失败了'
	
	for j in xrange(0,5):
		urlresult=[]
		
		#下面是访问一次答题的主页
		reauest_datiindex=urllib2_reuest(datiindex,useragent,cookies);#登陆的请求包，用来登陆到服务器
		#下面是访问14次获取题目的连接
		for x in xrange(14):
			reauest_question=urllib2_reuest(getquestions,useragent,cookies);#登陆的请求包，用来登陆到服务器
			questionss=reauest_question.read()#questionss是str类型
			# print questionss
			# print  type(questionss)
			null = ''#因为此处处理的是字符，所以此处定义为空字符串
			true='true'
			false='false'
			global null#解决eval()转换字符串的时候无法转换null的问题
			global true
			global false
		
			tem=questionss.decode("utf-8")#将内存中的questionss以str类型读出
			question=eval(tem)#将str字符串转化为字典 #用eval转换而不用json.load是因为这个转换时汉字容易编码
			# print question
		
			# question=json.loads(questionss)#question是字典类型
			# print  type(question)# reauest_question.read();#encode('iso8859-1')
			print '打印结束'
		
			for i in xrange(len(question['obj'])):
				ques=question['obj'][i]#五道题的第几题，是一个字典
				# print '打印第  %d  道题目：'%(i+1),len(question['obj'])
				# print ques#字典
				# print type(ques)
				temp={"id":"402880a951579cfb015157b773d80f6b","answer":"啊"}
				# tt='是'#<type 'unicode'>
				# print type(ques['rigthAnswers'])#ques['rigthAnswers']是<type 'str'>
				# tt=ques['rigthAnswers']#.decode("gbk")
				# print tt#<type 'unicode'>
				temp["answer"]=ques['rigthAnswers']
				temp["id"]=ques['id'];
				# print temp["id"],temp["answer"]
				urlresult.append(temp)
		
				# if len(temp["answer"])>maxlen and len(temp["answer"])<6 :
				# 	maxlen=len(temp["answer"])
				# 	cishu=1
				# 	print temp["answer"]
				# 	pass
				# elif len(temp["answer"])==maxlen :
				# 	cishu+=1
				# 	print temp["answer"]
				# elif temp["answer"]=='ABCDEF' :
				# 	maxlen=5
				# 	cishu=1
				# print cishu,maxlen 
		
				# print i, "anstemp是字典：",str(temp)
				#字典整体输出时，里面的中文会以\xe6\xad\xa3 utf8编码来直接打印出来，但是如果将字典里面的value提取出来打印的话，中文就正常显示
				#anstemp是字典： {'answer': '\xe6\xad\xa3\xe7\xa1\xae', 'id': '402880a951579cfb015157a4720707f0'}
				# print i, "urlresult是字典：",str(urlresult)
				pass
			pass
		
		# print '字典长度为：',len(urlresult)
		urlresult=urlresult[0:zhengque[j]]#正确题目数量
		# urlresult.extend(rightans[0:right])
		# print '字典长度为：',len(urlresult)
		urlresult.extend(wrongans[0:cuowu[j]-1])#错误题目数量
		print '字典长度为：',len(urlresult)
		print num
		#下面是提交答案并且获取得分
		urltem=json.dumps(urlresult,ensure_ascii=False)#将字典转换成字串(默认是Unicode类型的)
		urltem=urltem.replace(' ', '')#urltem.replace('\'', '\"')
		print "字典如下："
		# print urltem
		# print type(urltem)#urltem是<type 'unicode'> 类型 
		# a=urltem.encode("utf-8")#utf-8编码后a是<type 'str'>类型即：.encode("utf-8")将Unicode转换成str类型
		# print type(a)
		urltem=urllib.quote(urltem)#urllib.quote()只接受str类型的字串，不接受Unicode类型的，所以必须.encode("utf-8")将Unicode编码为str类型
		answerurl=answer+urltem
		# print answerurl
		reauest_answer=urllib2_reuest(answerurl,useragent,cookies);#登陆的请求包，用来登陆到服务器
		print reauest_answer.read()
		# answerresp=json.load(reauest_answer)
		# print answerresp['msg'];
		
		# print type(urltem)
		
		# print json.dumps(urltem)
	print '五次成功完成'
	num=num+1
	pass
print '全部成功完成',num
