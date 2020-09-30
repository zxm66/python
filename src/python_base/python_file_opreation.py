# 文件操作。
# 想一个问题是：python如何实现内置函数的。就现在的这个python而言，有点像c++ 既可以面向过程 有可以面向对象编程。还有需要自己多写代码才能不断熟悉python的语法。不是仅仅地看视频。
#

def read_test():
    # mode='r' 只能读取
    # mode='w' 写入
    # mode='rb' 以二进制读取
    # mode='wb' 以二进制写入
    # mode='a' 追加
    # mode='r+' 可读写 没有文件会报错
    # mode='w+' 可读写 没有文件会创建
    f = open(file="./README.md",mode='r',encoding='utf8')
    print(type(f))
    x  = f.read()
    print(type(x))
    print(x)
    f.close()
    pass

def write_test():
    f = open("file_test.md",'w')
    f.close()
    pass

def seek_test():
    f = open("file_test.md","w+")
    f.write("hello world")
    # 改变文件光标的位置
    f.seek(0,0)
    x = f.read()
    print(x)
    f.close()
    pass

# rb 模式读取 没有文件会报错
def read_test_1_m():
    f = open('README.md','rb')
    while True:
        content = f.read(1024)
        print(content)
        if not content:
            break
    f.close()
    pass

def readlines_test():
    f = open("README.md",'r')
    content = f.readlines()
    print(content)
    f.close()
    pass

# 复制文件
def copy_file_test(source_file,target_file):
    sf = open(source_file,'r')
    content = sf.read()
    tf = open(target_file,'w+')
    tf.write(content)
    sf.close()
    sf.close()
    pass
# open 参数 file 指定打开的文件。 mode 打开文件使用的方式。默认是r 只读。 encode 打开文件的编码方式
if __name__ == "__main__":
    copy_file_test("README.md","hello_world.txt")
    pass
