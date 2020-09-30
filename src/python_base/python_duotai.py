# 父类引用指向子类对象。
# 多态 基于继承的。通过不通的子类对象调用父类方法。得到不同的结果。

class Person(object):
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        pass

    def sleep(self):
        print("{} is sleeping".format(self.name))
        pass

    def __str__(self) -> str:
        return "this person's name is {}".format(self.name)
    pass


class Student(Person):

    def __init__(self,name,age,school) -> None:
        super(Student,self).__init__(name,age)
        self.school = school
        pass
    
    def sleep(self):
        print("{} is sleeping in classroom".format(self.name))
        pass


    def learn(self):
        print("{} is learning".format(self.name))
        pass
    pass


class Tiger(object):
    
    def __init__(self,name) -> None:
        self.name = name
        pass
    # 不写参数的类型的应该是object
    def eat(self,person:Person):
        print("{} is eated by {}".format(person,self.name))
        pass
    pass

if __name__ == "__main__":
    print(Student.__mro__)
    s = Student("zhangsan",22,"sizhong") 

    t = Tiger("xxx")
    t.eat(s)


    s.sleep()


    pass
