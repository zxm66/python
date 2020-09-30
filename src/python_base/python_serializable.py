
# python 的序列化和反序列化的操作,将数据从内存中保存到硬盘的过程，将数据从硬盘加载到内存的过程


import json

def serial_and_file_opearation():
    file = open('names.txt','w',encoding='utf8')
    file.write('只能写字符串，或者是二进制，不能写数字，不能写列表')
    file.close()
    pass

# 只能写入字符串，或者是二进制。将数据转换成为字符串或者是二进制
# json的本质是字符串？我觉的没有问题。一个东西不在内存中的东西。就是个字符串。
# 将数据转换成为二进制，使用picket这个模块
# 更多的使用是json。这也没有提序列化的本质。编码和解码是什么玩意儿。
if __name__ == "__main__":
    x = json.dumps(['name','age'])
    print("this x is {}, and the type of x is {}".format(x,type(x)))

    # json 将数据持久化，dumps将数据转换成为json字符串。
    # dump 直接上数据转换成为字符串的同时写入到指定文件。

    
    file = open('names.txt','w',encoding='utf8')
    json.dump(['name','sex'],file)
    file.close()

    # json 反序列化的方法 loads 将字符串加载成为python的数据。
    # load 读取文件，将读取的内容加载成为python的数据。 
    data = json.loads('{"name":"zhangxiaomin","sex":"M"}')
    #
    print("this data is {}, and the type of data is {}".format(data,type(data)))

    file = open('names.txt','r',encoding='utf8')
    data = json.load(file)
    print("this data is {}, and the type of data is {}".format(data,type(data)))
    file.close()

    pass
