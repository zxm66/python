class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Teen(object):
    pass

class Student(Person,Teen):
    pass


if __name__ == "__main__":
    p1 = Person("zhangsan",13)
    p2 = Person("zhangsan",13)
    # is 比较的是内存地址
    print(p1 is p2)

    a = 1
    if type(a) == int:
        print("the class of a is int")

    if type(p1) == Person:
        print("p1 is the instance of Person")

    s1 = Student("Tom",11)
    print(type(s1) == Student)
    print(type(s1) is Student)
    print(type(s1) == Person)
    print(type(s1) is Person)
    # isinstance 判断一个对象是否由指定类（或者是父类）实例化出来的
    print(isinstance(s1,Student))
    print(isinstance(s1,Person))
    print(isinstance(s1,(Student,Teen)))

    print(issubclass(Person, Student))
    print(issubclass(Student, Person))
    pass
