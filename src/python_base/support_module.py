#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__=['hello','support_print']
hello="hello"
world="world"
def support_print(obj):
    __import__('pprint').pprint("this is support_print method")
    pass
