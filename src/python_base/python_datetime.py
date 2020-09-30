
import datetime as dt
# 换个名字
from pprint import pprint as pp

# 以一个下划线开始 _ 不能用
if __name__ == "__main__":
    pp(dt.datetime.now())# 获取当前时间
    pp(dt.date(2020,1,1))#创建一个日期
    pp(dt.time(18,23,45))#创建一个时间
    pp(dt.datetime.now() + dt.timedelta(3)) # 计算三天以后的日期时间
    pass
