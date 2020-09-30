import os
from pprint import pprint

# os 模块中的path是经常使用的
if __name__ == "__main__":
    # opreation system name
    pprint(os.name)
    # 目录分隔符
    pprint(os.sep)
    # 拿到绝对路径
    pprint(os.path.abspath("src/"))
    # 判断是不是目录
    pprint(os.path.isdir("src/"))
    # 判断是否是文件
    pprint(os.path.isfile("src/"))
    #判断是否存在
    pprint(os.path.exists("src/"))
    # 获取文件名和文件拓展名
    pprint(os.path.splitext("1.txt"))
