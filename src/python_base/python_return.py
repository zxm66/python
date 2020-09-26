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

# 可变参数的使用

def add_many(nums):
    x = 0;
    for item in nums:
        x+=item
    
    return x

nums = [1,2,3,4,5,6]

# 列表
print("this sum is {}".format(add_many(nums)))



# *args 是个可变参数,多出来的参数会已元祖的方式保存到args
# 本质上应该是一个元祖。使用了*号。
def add(a,b,*args):
    print("this a is {},this b is {}".format(a,b))
    print("this args is {}".format(args))
    c = a + b;
    for arg in args:
        c += arg
    return c


print("this sum is {} ".format(add(1,2,3)))


# 除了使用def 还可以使用lambda

mul = lambda a,b:a*b #匿名函数 只用一次。

print("this mul is {}".format(mul(1,2)))

# 把函数当作参数去传递



