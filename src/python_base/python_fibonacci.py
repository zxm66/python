import time
class Fibonacci(object):

    def __init__(self,count) -> None:
        self.count = count
        self.index = 1
        self.value_pre = 1
        self.value_index=1 
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < self.count:
            self.value_pre = self.value_index
            self.value_index = self.value_index + self.value_pre
            return self.value_index
        else:
            raise StopIteration
    pass

if __name__ == "__main__":
    f = Fibonacci(12)
    print( f.__str__())
    print("hello world")
    for item in f:
        print(item)
        pass
    pass
