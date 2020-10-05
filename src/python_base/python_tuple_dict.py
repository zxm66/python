
def tuple_test(param,*args):
    print("this param of tuple_test is {}".format(param))
    print("this args of tuple_test is {}".format(args))
    print("this * args of tuple_test is {}".format(*args))
    #print("this type of  * args of tuple_test is {}".format(type(*args)))
    pass

def dict_test(param,**kwargs):
    print("this param of dict_test is {}".format(param))
    print("this kwargs of dict_test is {}".format(kwargs))
    print("this *kwargs of dict_test is {}".format(*kwargs))
    #print("this **kwargs of dict_test is {}".format(**kwargs))
    #print("this type of *kwargs of dict_test is {}".format(type(*kwargs)))
    pass

def tuple_dict_test(param,*args,**kwargs):
    print("this param of tuple_dict_test is {}".format(param))
    print("this args of tuple_dict_test is {}".format(args))
    print("this * args of tuple_dict_test is {}".format(*args))
    print("this kwargs of tuple_dict_test is {}".format(kwargs))
    print("this *kwargs of tuple_dict_test is {}".format(*kwargs))
    #print("this **kwargs of tuple_dict_test is {}".format(**kwargs))
    #print("this type of *kwargs of tuple_dict_test is {}".format(type(*kwargs)))
    pass


if __name__ == "__main__":
    # this * args of tuple is a
    tuple_test('hello tuple','a','b','c')
    # this * kwargs of dict is zhangsan
    dict_test('hello dict',zhangsan='zhang',lisi='li',wangwu='wang')
    tuple_dict_test('hello dict','a','b','c',zhangsan='zhang',lisi='li',wangwu='wang')
    pass
