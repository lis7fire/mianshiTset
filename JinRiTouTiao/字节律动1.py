#!/usr/bin/python3
#coding=utf-8
import sys

word=['hot']
dic=['doh', 'got'  , 'dot' , 'god' , 'tod'  , 'dog' , 'lot' , 'log']


w = ['hot']
dic = ['doh', 'got', 'dot', 'god', 'tod', 'dog', 'lot', 'log']
outli=[]
def getT(num,li):
    print('gesu为：',num)
    print('周期为：',li)
    xmax=li[num-1]-li[0]
    xmin=li[1]-li[0]
    for a in range(num):
        pass
    print(xmin)
    global outli
    outli.append(xmin)
    pass

def out(outlist):
    for x in outlist:
        print(x)
    

def main():
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        num=values[0]
        getT(num,values[1:])
    global outli
    out(outli)


if __name__ == '__main__':
    main()