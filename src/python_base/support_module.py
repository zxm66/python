#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__=['hello','support_print']
hello="hello"
world="world"
def support_print(obj):
    __import__('pprint').pprint("this is support_print method")
    pass

_support_print = support_print

if __name__ == "__main__":
    _support_print('hello world')
    pass
