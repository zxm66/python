
# 单例设计模式


class Singleton:
    # 私有变量
    __instance = None
    __is_first = True
    @classmethod
    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        else:
            pass
        return cls.__instance
    

    # init 这个方法将引用指向对应的内存空间
    def __init__(self,a,b) -> None:
        if self.__is_first:
            self.a = a
            self.b = b
            self.__is_first = False

    def __str__(self):
        return "a is {} and b is {}".format(self.a,self.b)

# 定义一个类，记录通过这个类创建了多少个对象
class Person:
    __count = 0
    def __new__(cls,*args,**kwargs):
        return object.__new__(cls)

    def __init__(self,name,age) -> None:
        Person.__count += 1
        self.name = name
        self.age = age

    def __str__(self):
        return "name is {} and age is {}".format(self.name,self.age)

    @classmethod
    def get_count(cls):
        return cls.__count

if __name__ == "__main__":
    p1 = Person("zhangsan",13)
    p2 = Person("lisi",22)
    print(p1)
    print(p2)

    p3 = object.__new__(Person)
    # 不调用__init__为什么会报错呢
    p3.__init__("wangwu",23)
    print(p3)

    print(Person.get_count())

    s1 = Singleton(1,2)
    s2 = Singleton(2,3)

    print(s1 is s2)
    print(s1)
    print(s2)

    pass
