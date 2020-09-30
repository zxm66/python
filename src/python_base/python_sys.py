from pprint import pprint
import sys
# 系统相关的模块
# 和文件操作相关的。设置标准化的输入输出
if __name__ == "__main__":
    s_in = sys.stdin
    # 读取键盘的输入
    #content = s_in.read()
    # 读了一个换行符
    #print(content)
    # 读了一个换行符号
    content = s_in.readline()
    print(content)
    
    while True:
        content = s_in.readline().rstrip('\n')
        if content == '':
            break
        print(content)
    
    sys.stdout = open("stdout.txt",'w',encoding='utf8')
    sys.stderr = open("stderr.txt",'w',encoding='utf8')
    print(1/0)

    #sys.stdin #接收用户的输入,标准输入流 等同于input()
    #sys.stderr 标准错误输出流
    #sys.stdout 标准输出流
    #x = input("please input some string")
    #pprint(x)
    
    # 查找模块的路径(不是系统的环境变量)
    pprint(sys.path)
    # 退出程序 参数退出码0
    sys.exit(0)
    pprint("hello python")
    pass
