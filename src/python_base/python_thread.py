 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
# python 多线程,只有执行结束之后，vim的窗口才会弹出来
 
import time
import threading
class Person(object):
    def __init__(self,name) -> None:
        self.name = name
        pass
    def dance(self):
        for i in range(5):
            time.sleep(0.1)
            print("{} is dancing".format(self.name))


    def sing(self):
        for i in range(5):
            time.sleep(0.1)
            print('{} is singing'.format(self.name))
    pass

if __name__ == '__main__':
    p = Person('hexiaohan')
    # 还有要解决的一个问题是，然后查看python的源码。想想这个是一个什么样的问题：
    # python代码是不需要编译，只需要解释的，也就是不会像java一样存在class文件。
    # 那么查看python的源码这个操作理论上是相比较java是简单的。
    # java的源码，重新使用class反编译出来新的java文件吗？？
    t1 = threading.Thread(target=p.dance)
    t2 = threading.Thread(target=p.sing)

    t1.start()
    t2.start()
    pass
