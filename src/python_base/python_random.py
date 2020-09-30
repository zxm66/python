
# random 模块的使用

from pprint import pprint
import random

if __name__ == "__main__":
    # randint(a,b) 生成a到b的随机数 包含开始和结尾 = random.randrange(a,b+1)
    pprint(random.randint(1,10000))
    # 生成[0,1)的浮点数
    pprint(random.random())
    # 和randint的区别是不包含右边界
    pprint(random.randrange(1,10000))
    # choice 用于在可迭代对象里边随机抽取一个数据
    pprint(random.choice(["zhangsan","lisi","wangwu","zhaoliu"]))
    # sample 用于在可迭代对象里边随机抽取n个数据
    print(random.sample(["zhangsan","lisi","wangwu","zhaoliu"],2))
    pass

