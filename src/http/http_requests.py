#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
import sys 
 
import requests
#导入json包
import json
 
if __name__ == '__main__':
    #设置要访问的地址（这里是get请求）
    url = 'http://api.map.baidu.com/geocoding/v3/?address=保定市定兴县开放路&output=json&sn=071c4d942b201cf46aedf59033074c81&ak=3Ih4sYMVYhmI6xUmLFc2ROGTs28yN5DK'
    #直接请求
    r = requests.get(url)

    #用自带的json工具把字符串转成字典
    dictinfo = json.dumps(r.text)
    #输出字典
    print(dictinfo)
