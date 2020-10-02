from collections.abc import Iterable
# python的可迭代对象。list/tuple/dict/set/str/range/filter/map
# for .. in + 可迭代对象
class Demo(list):
    pass
class Demo2(object):

    def __init__(self):
        self.count = 0
        pass

    def __iter__(self): # 只要重写了 __iter__方法就是一个可迭代对象
        return Demo2()
    pass

    # for in 循环的本质 是不断调用这个__next__方法
    def __next__(self):
        self.count += 1
        if self.count < 5:
            return 'hello'
        else:
            raise StopIteration

if __name__ == "__main__":
    d = Demo(('demo1','demo2'))
    d2 = Demo2()
    # list() 创建一个list对象
    l = list(('lisi','zhangsan'))
    print(isinstance(d,Iterable))
    print(isinstance(d2,Iterable))
    print(isinstance(l,Iterable))
    # 什么是可迭代对象？ 什么是迭代器？
    # Iterable Iteror
    for item in l:
        print(item)
        pass
    for item in d:
        print(item)
        pass
    pass
    # for 循环的本质就是调用可迭代对象。 __iter__方法。获取到这个方法的返回值。
    # 这个返回值需要是一个对象。然后不断地调用这个对象的 __next__方法(要让这个next方法结束，就需要是一个迭代器对象)
    for item in d2:
        print(item)
        pass
    









