# 继承的使用
# 封装 继承 多态
# 封装 

class A(object):
    def demo(self):
        print("this is class of A method demo")

class AA(A):
    def demo(self):
        print("this is class of AA method demo")

class B(object):
    def demo(self):
        print("this is class of B method demo")



class BB(B):
    def demo(self):
        print("this is class of AA method demo")

# 看来不能同时继承A和AA，也就是关系是线性的。
class C(AA,BB):
    pass
if __name__ == "__main__":
    c= C()
    # 先到先得(深度优先还是广度优先？？？？,深度优先)
    print(C.__mro__)
    # 可以看出来的是这个继承的机制是延续了C++的机制了。
    c.demo()
    
    pass


