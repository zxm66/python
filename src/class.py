#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student:

    def __init__(self):
        print "this is the function of init"
        pass
    def __sayHello__(self):
        return "hello"



s = Student()
print s.__sayHello__()
print s.__class__
