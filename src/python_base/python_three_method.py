
class Person(object):

    @staticmethod
    def __new__(cls,*args,**kwargs):
        return object.__new__(cls)

    def __init__(self):
        pass

if __name__ == "__main__":
    pass
