#!/usr/local/env python
# -*- coding:utf-8 -*-

import redis   # 导入redis 模块

r = redis.Redis(host='192.168.43.97', port=6379, db=0)

r.set('name', 'runoob')  # 设置 name 对应的值
print(r['name'])
print(r.get('name'))  # 取出键 name 对应的值
print(type(r.get('name')))  # 查看类型



