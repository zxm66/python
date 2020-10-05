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
        self.type=Person.type

    def __str__(self):
        """
        ** 两个星号是表示任意长度的字典吗？
        * 一个星号是表示任意长度的list或者是set吗？
        百度解释：
        *args 参数是一个元祖
        ** kwargs 参数是一个字典。
        """
        print(self.__dict__)
        print(*self.__dict__)
        print("name is {name},age is {age},type is {type}".format(**self.__dict__))
        return "name is {},age is {},type is {}".format(self.name,self.age,self.type)

if __name__ == "__main__":
    print("this is me")
    print('hello world')
    p = Person("zhangsan", 13)
    print(p)
    # 只是给p加了一个对象属性
    p.type = "people"
    print(p)
    Person.type = "person.type"
    print(Person.type)
    print(p.type)
    pass
