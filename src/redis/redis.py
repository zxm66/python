#!/usr/local/env python
# -*- coding:utf-8 -*-
# 导入redis 模块
import redis
r = redis.Redis(host='192.168.43.97', port=6379, db=0)
r.set('name', 'runoob')
print(r['name'])
print(r.get('name'))
print(type(r.get('name')))
