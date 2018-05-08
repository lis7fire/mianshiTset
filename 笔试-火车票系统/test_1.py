#!/usr/bin/python3
# coding: utf-8
# 上面两句注释必须要，防止无法打印中文的

import datetime
import os
from pyquery import PyQuery as pq

class chechout(object):
	"""docstring for chechout"""
	def __init__(self, arg):
		super(chechout, self).__init__()
		self.arg = arg
		self.buyed={}
		self.checked={}

	def write_file(self,fname,str):
		# fname='./b.txt'
		fileout=open(fname,'a')
		fileout.write(str)
		fileout.write("\n")
		fileout.close()
		pass

	def read_file(self,fname):
		# fname='./a.txt'
		filein=open(fname,'r')
		self.buyed={}
		while 1:
			line=filein.readline()
			if line:
				sfid=line.split(' ')[1].strip().lstrip()
				name=line.split(' ')[0].strip().lstrip()
				print(line,sfid,name)
				self.buyed[sfid]=name
			else:
				break
		filein.close()
		print(self.buyed)

	def checkin(self,sfid):
		print(self.buyed)
		if sfid in self.buyed.keys():
			print('checkin true')
			self.write_file('./b.txt',self.buyed[sfid]+' '+sfid)
			return True
		else:
			print('checkin false 未写入文件')
			return False
		pass

	def buy(self,name,sfid):
		if sfid in self.buyed.keys():
			print('已经买了,buy False')
			return False
		self.write_file('./a.txt',name+' '+sfid)
		self.buyed[sfid]=name
		print(name,'购买成功',sfid)
		return True
		pass

	def tui(self,name,sfid):
		if sfid in self.buyed:
			del self.buyed[sfid]
			for key in self.buyed:
				self.write_file('./a.txt',self.buyed[key]+' '+key)
			return True
		else:
			print("还没有买票")
			return False
		pass

a=chechout('a')
a.read_file('./a.txt') #先初始化
# a.write_file('./b.txt','as 125')
# a.buy('sd','1255')
a.checkin('1255')
# a.tui('qw','123')tui
# 