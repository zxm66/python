# 类属性只能使用类修改，不能用实例修改

class Person:
    # 类属性
    type = "person"
    def __init__(self,name,age) -> None:
        """
        对象属性
        """
        self.name = name
        self.age = age

    def __str__(self):
        return "name is {},age is {},type is {}".format(self.name,self.age,self.type)




if __name__ == "__main__":
    print(Person.type)
    p = Person("zhangsan", 13)
    print(p)
    # 只是给p加了一个对象属性
    p.type = "people"
    print(p)
    Person.type = "person.type"
    print(Person.type)
    print(p.type)
    pass
