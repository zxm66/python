#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student:

    def __init__(self):
        __import__('pprint').pprint("this is the function of init")
        pass
    def __sayHello__(self):
        return "hello"


class Teacher:
    name = ""
    age = 0

    def __init__(self):
        pass
    def __sayHello__(self):
        return "hello"
    def __toString__(self):
        return "name:"+self.name +",age:"+str(self.age)

s = Student()
__import__('pprint').pprint(s.__class__)
__import__('pprint').pprint(s.__sayHello__())

t = Teacher()
t.name = "zhangxiaomin"
t.age = 18

__import__('pprint').pprint(t.__toString__())
