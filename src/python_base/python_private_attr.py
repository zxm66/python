

class Person:
    def __init__(self,name,age,money=1000):
        self.name = name
        self.age = age
        #私有变量
        self.__money = money
        pass

    def change(self):
        self.__money += 10
        pass

    # getter setter 方法
    def getMoney(self):return self.__money
    def setMoney(self,money):self.__money = money
    
    # 私有函数
    def __test(self):
        print("hello test")




if __name__ == "__main__":
    p = Person("zhangsan",12,2000)
    print(p.getMoney())
    p.setMoney(3000)
    print(p.getMoney())
    p.change()
    #print(p.__money)
    print(p._Person__money)
    #p.__test()
    p._Person__test()
