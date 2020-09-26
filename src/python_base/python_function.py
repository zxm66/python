from functools import reduce

def calc(a,b):return add(a,b)
def add(a,b):return a + b
def minus(a,b):return a - b
def foo(a):return a["height"]
# 函数作为参数传递
# 也就是有了一个函数类型
# c语言里边有一个东西叫做函数指针
def function(a,b,fn):return fn(a,b)
def function2():
    __import__('pprint').pprint("this is function2")
    return function
if __name__ == "__main__":
    __import__('pprint').pprint("this clac is {}".format(calc(1,2)))
    __import__('pprint').pprint("this function 's result is {}".format(function(1,2,add)))
    # 使用lambda
    __import__('pprint').pprint("this function 's result is {}".format(function(2,3,lambda a,b:a*b)))
    # python 的内置函数，内置类
    nums = [4,8,2,1]
    nums.sort()
    __import__('pprint').pprint("this nums is {}".format(nums))
    students = [
        {"name":"zhangsan","age":18,"score":98,"height":180},
        {"name":"lisi","age":19,"score":99,"height":170}
    ]
    # key的参数类型是个函数
    students.sort(key=foo)# 在sort内部实现的时候，调用了foo方法。并且传入了一个参数 foo的参数是一个dict
    __import__('pprint').pprint("this students is {}".format(students))
    students.sort(key= lambda item:item["age"])
    __import__('pprint').pprint("this students is {}".format(students))
    # filter 可对迭代对象进行过滤,得到的是一个filter对象，python2的时候内置函数，python3是个内置类
    students = filter(lambda item:item["height"]>170,students)
    __import__('pprint').pprint("this students is {}".format(list(students)))
    # map 和java的操作一样样的
    # reduce 以前是一个内置类，内置函数和内置类都在builtins.py文件
    scores = [100,11,223,111]
    #__import__('pprint').pprint("this reduce 's result is {}",reduce((lambda a,b:a+b),scores)) 
    # 返回函数
    __import__('pprint').pprint(function2()(1,2,add))
    
    pass


