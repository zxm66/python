 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
# python 多线程,只有执行结束之后，vim的窗口才会弹出来
 
import os
import time
import threading
class Person(object):
    def __init__(self,name) -> None:
        self.name = name
        pass
    def dance(self):
        for i in range(5):
            time.sleep(0.1)
            print("the pid of os is {},the current thread is {},{} is dancing".format(os.getpid(),threading.currentThread().name,self.name))


    def sing(self):
        for i in range(5):
            time.sleep(0.1)
            print('the pid of os is {},the current thread is {},{} is singing'.format(os.getpid(),threading.currentThread().name,self.name))
    pass


def test1():
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


class Ticket(object):
    lock = threading.Lock()
    def __init__(self):
        self.count = 100
        pass
    pass

    def sell_ticket(self):
        
        while True:
            # 加锁
            Ticket.lock.acquire()
            if self.count > 0:
                time.sleep(0.01)
                self.count -= 1
                print("the current thread is {}, and the count of ticket is {}".format(threading.currentThread().name,self.count))
                # 释放锁
                Ticket.lock.release()
            else:
                Ticket.lock.release()
                break
        pass

def test2():
    t = Ticket()
    t1 = threading.Thread(target=t.sell_ticket,name='thread 1')
    t2 = threading.Thread(target=t.sell_ticket,name='thread 2')

    t1.start()
    t2.start()
    pass

# 线程之间的通信
# 生产者  消费者。 queue 结构可以在不同的线程之间通信 先进先出
import queue
class Message(object):
    q = queue.Queue()
    def produce(self):
        for i in range(10):
            time.sleep(0.01)
            print("produce number i is {}".format(i))
            Message.q.put('{} {}'.format(threading.currentThread().name,i))
            pass
        pass
    def consumer(self):
        for i in range(10):
            time.sleep(0.01)
            print('consume number i is {}'.format(Message.q.get()))
        pass

def test3():
    m = Message()
    p2 = threading.Thread(target=m.produce,name='produce2')
    p1 = threading.Thread(target=m.produce,name='produce1')
    c = threading.Thread(target=m.consumer,name='consumer')
    p2.start()
    p1.start()
    c.start()
    pass
# 栈结构stock 后进先出 

# 多进程。 进程的状态

import multiprocessing
def test4():
    p = Person('zhangsan')
    # target 用来表示执行的任务
    # args 用来传参 类型是一个元祖
    p1 = multiprocessing.Process(target=p.dance)
    p2 = multiprocessing.Process(target=p.sing)
    
    p1.start()
    p2.start()
    pass

if __name__ == '__main__':

    pass



























