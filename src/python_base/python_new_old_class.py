# 手动指定父类object
class Student(object):
    pass

# 默认是继承object
class Dog:
    pass

# 新式类(继承自object)，经典类(不继承自object) ，区别在python2里，不指定一个类的父类是object，这个类是经典类
if __name__ == "__main__":
    pass
