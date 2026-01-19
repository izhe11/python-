import numpy as np

arr1 = np.array([[1,2,3],[12,35,21]])
arr2 = np.array([5,8,10])
arr3 = np.arange(2,12,2)     #start,end,step
arr4 = np.linspace(0,12,4)   #等间隔分段，0-12分4份

arr5 = np.eye(3)             #创建单位矩阵
arr6 = np.diag([1,2,3])      #创建对角矩阵
arr7 = np.array([1,1,1])

np.sqrt(arr2)                #可以直接对数组、矩阵进行平方根、三角函数、对数指数等等运算

print(arr6)
print(np.sqrt(arr2))
print(arr2+arr7)             #可以对array数组或矩阵直接进行加减乘除运算

# print(arr1.size)
# print(arr1.dtype)
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3)
# print(arr4)