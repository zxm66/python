

# with 关键字,自动关闭连接
# with 实际上是一个上下文管理器
# 语句后边的结果对象。需要重写__enter__和__exist()__
# 当进入with模块时，自动调用__enter__方法的代码
# 当with代码块完成以后，自动调用__exit__方法



class Person(object):
    

    def eat(self):
        print("{} is eatting".format(self))
        pass
    def __enter__(self):
        print("this is __enter__ method")
        return "this self is {}".format(self)

    def __exit__(self,ext_type,exc_val,exc_tb):
        print("this self is {},this ext_type is {},this exc_val is {},this exc_tb is {}".format(self,ext_type,exc_val,exc_tb))
        pass
    pass

    


def with_test():

    with open('README.md','r') as file:
        # 不需要手动关闭文件
        x = file.read()
        print(x)
        pass
    pass

if __name__ == "__main__":
    with Person() as p:
        print(p)# 只有在调用p的时候会执行__enter__方法。
        pass
    pass
