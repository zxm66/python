
import hello_world

# 这个文件用来测试main函数的作用，在于倒入的时候执行不执行代码，非常想c程序的include
__import__('pprint').pprint("this is hello python")
print(hello_world.__doc__)
