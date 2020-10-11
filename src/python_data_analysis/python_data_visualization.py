 
######################################################################
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
import pandas as ps
from matplotlib import pylab as plt
 
def test():
    x = [1,2,3]
    y = [1,4,9]
    z = [10,5,0]
    plt.plot(x,y)
    plt.plot(x,z)
    plt.title('test plot')
    plt.xlabel('x')
    plt.ylabel('y and z')
    plt.show()
    pass
def test1():
    simple_data = ps.read_csv('~/Downloads/sample_data.csv')
    print(simple_data)
    print(type(simple_data))
    print(simple_data.columns)
    print(simple_data.column_c.iloc[1])
    
    plt.plot(simple_data.column_a,simple_data.column_b)
    plt.plot(simple_data.column_a,simple_data.column_c)
    plt.show()
    pass

def test2():
    data = ps.read_csv('~/Downloads/countries.csv')
    us = data[data.country == 'United States']
    china = data[data.country == 'China']
    plt.plot(us.year,us.population / 10**6)
    plt.plot(china.year,china.population / 10**6)
    plt.legend(['us','china'])
    plt.xlabel('year')
    plt.ylabel('population')
    plt.show()
    pass
if __name__ == '__main__':
    test2()
    pass















