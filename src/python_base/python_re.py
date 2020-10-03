#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 正则表达式，
# regular expression
# python中的正则表达式。
# 查找和替换 字符串。
def test1():
    x = 'hello\\world'
    """
    在正则表达式里，如果匹配一个\需要使用\\\\
    第一个参数是正则匹配的规则
    第二个参数表示需要匹配的字符串
    """
    m = re.search(r'\\',x)
    print("this m is {}".format(m))
    pass

def test2():
    """
    match 和 search的区别
    共同点：只对字符串查询一次
        返回类型都是re.Match类型的对象
    不同点：
        match是从头开始匹配 一旦匹配失败就返回None
        serch是在整个字符串里查找。
    """
    x = 'hello\\world'
    m = re.match(r'\\',x)
    print("this m is {}".format(m))

    pass

def test3():
    """
    match 和 search的区别
    共同点：只对字符串查询一次
        返回类型都是re.Match类型的对象
    不同点：
        match是从头开始匹配 一旦匹配失败就返回None
        serch是在整个字符串里查找。
    finditer 返回的结果是一个可迭代对象
    findall 把查找到的所有字符串放到一个列表中
    """
    x = 'hello\\world'
    m = re.finditer(r'\\',x)
    print("this m is {}".format(m))
    for item in m:
        print("this is the item {}".format(item))
        pass
    pass



def test4():
    """
    match 和 search的区别
    共同点：只对字符串查询一次
        返回类型都是re.Match类型的对象
    不同点：
        match是从头开始匹配 一旦匹配失败就返回None
        serch是在整个字符串里查找。
    finditer 返回的结果是一个可迭代对象
    findall 把查找到的所有字符串放到一个列表中
    """
    x = 'hello\\world8381x1'
    m = re.findall(r'x\d+',x)
    print("this m is {}".format(m))
    for item in m:
        print("this is the item {}".format(item))
        pass
    pass




def test5():
    """
    match 和 search的区别
    共同点：只对字符串查询一次
        返回类型都是re.Match类型的对象
    不同点：
        match是从头开始匹配 一旦匹配失败就返回None
        serch是在整个字符串里查找。
    finditer 返回的结果是一个可迭代对象
    findall 把查找到的所有字符串放到一个列表中
    """
    x = 'hello\\world8381x1'
    m = re.fullmatch(r'x\d+',x)
    print("this m is {}".format(m))
    pass



def test6():
    """
    match 和 search的区别
    共同点：只对字符串查询一次
        返回类型都是re.Match类型的对象
    不同点：
        match是从头开始匹配 一旦匹配失败就返回None
        serch是在整个字符串里查找。
    finditer 返回的结果是一个可迭代对象
    findall 把查找到的所有字符串放到一个列表中
    """
    x = 'hello\\world8381x1'
    m = re.fullmatch(r'x\d+',x)
    print("this m is {}".format(m))
    pass


def test7():
    m = re.search(r'm.*a','mdadskmbahefelids')
    # span 匹配到的结果字符串的开始和结束的下标
    print(m.span())
    print(m.group())
    print(m.group(0))
    # group 方法表示正则表达式的分组
    # 没有分组 默认只有一个
    # 分组的下标从0开始
    pass
# 首先要明白正则表达式是干什么用的。解析字符串的。
# 其次明白python处理处理正则表达式的api。
import re
if __name__ == "__main__":


    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()



    print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
 
    line = "Cats are smarter than dogs"
 
    matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
    if matchObj:
        print ("matchObj.group() : ", matchObj.group())
        print ("matchObj.group(1) : ", matchObj.group(1))
        print ("matchObj.group(2) : ", matchObj.group(2))
    else:
        print ("No match!!")

    pass

