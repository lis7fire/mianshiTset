#!/usr/bin/python3
#-*-coding:utf-8-*- 
import datetime
import os
from pyquery import PyQuery as pq
import pymysql.cursors
import sys

print('aaa')

class people:
	"""docstring for people"""
	def __init__(self, name,arg,high):
		self.age = arg
		self.name=name
		self.high=high

	def readme(self,arg):
		print(arg)
		
ls=people('king',20,178)
print("rrw")
while 0:
	kai=float(input("请输入开盘价:"))
	shou=float(input("请输入收盘价:"))
	shouyi=(shou-kai)*100/kai
	print('涨幅为: {0:.2f}%'.format(shouyi))
	pass


for x in range(0,2):
	print('================卖出：===================')
	print(x)
	pass

floders=open('E:\我的科研\本科生毕业设计最终汇总的\毕业设计总结\过程\OurNVMCFS\myNVMCFS\myfsold')
print(floders)
