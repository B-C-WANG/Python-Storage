import numpy as np


data = np.array([1,2,3,4,5])
data2 = np.array([1,2,3,4,5])
data3 = np.array([1,2,3,4,5])


data_a = map(lambda x:(x+1,x+2), data)

print("A")

for i in data_a:
    print(i)

data_b = map(lambda x,y:x+y, data,data2)


print("B")
for i in data_b:
    print(i)

print("C")
def sum(*val):
    return np.sum(val)

data_c = map(sum, data,data2,data3)
for i in data_c:
    print(i)

