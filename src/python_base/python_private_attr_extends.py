



class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("{} is eating".format(self.name))

    def __private_method(self):
        print("this is a private method,and self name is {}".format(self.name))


class Cat(Animal):
    def __private_method_1(self):
        print("this is a private method,and self name is {}".format(self.name))

if __name__ == "__main__":
    animal = Animal("zhangsan",12)
    animal.eat()
    animal._Animal__private_method()

    cat = Cat("cat",12)
    # 私有方法是不继承的
    #cat.__private_method()
    cat._Animal__private_method()
    pass
