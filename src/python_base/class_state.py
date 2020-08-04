#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student:

    def __init__(self):
        print "this is the function of init"
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
print s.__sayHello__()
print s.__class__

t = Teacher()
t.name = "zhangxiaomin"
t.age = 18
print t.__toString__()

