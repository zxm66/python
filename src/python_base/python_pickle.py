
# python 里存入数据只支持存入字符串和二进制
# pickle 将python里任意对象转换成为二进制


import pickle

# dumps 将python数据转换成为二进制
# dump 将python数据转换成为二进制，同时保存到指定文件

# loads 将二进制加载成为python对象
# load 读取文件，将文件加载成为python对象。
if __name__ == "__main__":
    names = ['zhangsan','lisi']
    # 将对象转换成为二进制
    b_names = pickle.dumps(names)
    print("this b_names is {}".format(b_names))
    # wb 二进制写入。
    # 不能传encoding
    file = open('names.txt','wb')
    file.write(b_names)
    file.close()
    # 二进制读出
    # 
    file = open('names.txt','rb')
    x =file.read()
    y = pickle.loads(x)
    print("this y is {}".format(y))
    file.close()


    file = open('names.txt','wb')
    pickle.dump(names,file)
    file.close()

    file = open('names.txt','rb')
    print(pickle.load(file))
    file.close()

    pass
