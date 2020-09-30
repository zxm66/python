# __new__ 申请内存空间
# __init__ self 指向申请的空间
#__ 两个下划线的方法是魔法方法
# 动态语言，动态类型


class Person:
    __slots__=('name','age','height') #这个属性直接定义在类里边。是一个元祖。用来规定对象可以存在的属性。
    def __init__(self,name,age,height) -> None:
        self.name = name
        self.age = age
        self.height = height
        pass

    def run(self) -> None:
        print("running........")
        pass
    def __str__(self):
        return "This person's name is {},age is {} and height is {}".format(self.name,self.age,self.height)

    def __eq__(self, o) -> bool:
        return self.name is o.name and self.age is o.age and self.height is o.height 
        
class Student(Person):
    """
    this is doc of student
    """
    #__slots__=()

    def learn(self) -> None:
        print("learn..........")
        pass
    pass

    def __call__(self):
        print("this is call method")
        pass
    
    def __del__(self) ->None:
        print("the object is deleted")
        pass

if __name__ == "__main__":
    str1 = "hello world"
    str2 = "hello world"
    print(str1 is str2)
    print(str1 == str2)
    stu1 = Student("zhangsan",12,180)
    stu2 = Student("zhangsan",12,180)
    # is 比较的地址 == 调用的是__eq__比较的是内容
    print(stu1 is stu2)
    print(stu1 == stu2)
    stu = Student("zhangsan",12,180)
    # 对象后边使用括号，需要写__call__方法
    print(stu())
    print(stu)
    # 类的内置属性
    print(dir(stu))
    print(stu.__doc__)
    stu.run()
    stu.learn()
    # 直接添加属性
    stu.city = "beijing"
    print(stu.city)
    print(type(stu))
    # stu 的type已经变化了
    stu = "hello world"
    print(type(stu))
    pass
