#!/usr/local/python
# -*- coding:UTF-8 -*-
value = (1,2)
print(type(value))
# array
var1 = [1,2]
print(type(var1))
# set 
var2 = {1,2,2}
print(type(var2))
for item in var2:
    print(item,sep=' ',end=' ')
    pass
var3 = {"name":"zhangxiaomin"}
print('\n')
print(type(var3))
var3 = {"name":"zhangxiaomin","age":18}
#使用{} 一个元素是set key/value是dict
var3 ={'name':'zhangsan','age':18}
print(type(var3))


