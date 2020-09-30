
# 将数据写入内存涉及到stringio和bytesio两个类
# python 中的流对象
from io import StringIO,BytesIO




if __name__ == "__main__":
    s_io = StringIO()
    s_io.write("hello")
    s_io.write(" world")
    print(s_io.getvalue(),sep="hhhhhhh",end="wwwwww")
    print("hello",file=open('hello_world.txt','w'))
    s_io.close()

    b_io = BytesIO()
    b_io.write("hello 你好 world".encode("utf8"))
    print(b_io.getvalue().decode("utf8"))
    b_io.close()

    pass
