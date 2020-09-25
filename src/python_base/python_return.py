#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
 
# 返回多个值，实质上是返回了个元祖
# 函数名也是一个标识符，遵循命名规范
# 

def get_sum(a,b):
    return a + b
def calc(a , b):
    shang = a/b;
    yushu = a%b;
    return shang,yushu
def test_return():
    return 1,"hello world"
if __name__ == '__main__':
    sum = get_sum(1,2)
    print("this sum is {}".format(sum))
    shang,yushu = calc(2, 3)
    print("this shang is {},and this yushu is {}".format(shang,yushu))
    number,string = test_return()
    print("this number is {}, and this string is {}".format( number,string))

# python 的缺省参数，或者说默认参数
# 这个只能使用python3执行，python2执行报错了。

print("hello","你好",sep = "-----")


def say_hello(name ,age,city="天津"):
    print("大家好，我是{},今年{}岁了，我来自{}".format(name,age,city))
    pass

# 位置参数，关键字参数，
say_hello("jack",24)

say_hello(age=12,name="zhangsan")




