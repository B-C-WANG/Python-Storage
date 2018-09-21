from functools import reduce

import numpy as np


data = np.array([1,2,3,4,5])
data2 = np.array([1,2,3,4,5])
data3 = np.array([1,2,3,4,5])

def add1(x,y):
    #return x * 2 # 2的五次方
    #return x + 1 # 2每次都加1
    #return  x     # x的最后一个值
    return x + y   # 计算 1 加到15


data_a = reduce(add1, data)
print(data_a)