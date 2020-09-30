class Calculator(object):

    @staticmethod
    def add(a,b):return a + b
    @staticmethod
    def minus(a,b):return a - b



class Person:
    type = "human"
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        pass
    def eat(self,food):print(self.name +" is eating "+ food)
    @staticmethod
    def test():print("this is static method")

    @classmethod
    def demo(cls):print("this is class method and {} is {}".format(cls,Person)) # cls is Person


if __name__ == "__main__":
    p =Person("zhangsan",18)
    Person.eat(p,"salad")
    Person.test()

    Person.demo()
    p.demo()

    print(Calculator.add(1,1))
    print(Calculator.minus(1,1))
    
    pass
