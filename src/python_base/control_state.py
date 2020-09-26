#!/usr/local/python
# -*- coding:UTF-8 -*-

for letter in "python":
    __import__('pprint').pprint("this letter is {}".format(letter))
var1 = {"name":"zhangxiaomin","age":18}

for key in var1.keys():
    __import__('pprint').pprint("this key is {}".format(key))
