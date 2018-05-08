#!/usr/bin/python3
# coding: utf-8
# 上面两句注释必须要，防止无法打印中文的

import datetime
import os
from pyquery import PyQuery as pq
import sys 

a=input("请输入")
# str1=raw_input("请输入")
print(a)

#输入多组数据并输出 
for line in sys.stdin: 
	for value in line.split(): 
		print(value)

