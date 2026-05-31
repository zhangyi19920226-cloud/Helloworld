import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)   # (2,3)   → 2行，3列
print(arr.size)    # 6       → 元素总数
print(arr.ndim)    # 2       → 维度数
print(arr.dtype)   # int64   → 数据类型
print(arr.itemsize)  # 8      → 每个元素占用的字节
print(arr.nbytes)   # 48      → 数组占用的总字节
print(arr.data)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

sum_axis0 = np.sum(arr, axis=0)   # 以行为维度沿行方向计算，即把每一列的数相加 → [5,7,9]
sum_axis1 = np.sum(arr, axis=1)   # 以列为维度沿列方向计算，即把每一行的数相加 → [6,15]
mean_axis0 = np.mean(arr, axis=0)  # 以行为维度沿行方向计算平均值 → [2.5,3.5,4.5]
mean_axis1 = np.mean(arr, axis=1)  # 以列为维度沿列方向计算平均值 → [2.0,5.0]
print("沿行方向求和:", sum_axis0)
print("沿列方向求和:", sum_axis1)
print("沿行方向求平均值:", mean_axis0)
print("沿列方向求平均值:", mean_axis1)

a = np.arange(15).reshape(3, 5)
a
print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.dtype.name)
print(a.nbytes)
print(type(a))
b = np.array([6, 7, 8])
b
print(type(b))


np.zeros((3, 4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
np.ones((2, 3, 4), dtype=np.int16)
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]], dtype=int16)
np.empty((2, 3))
array([[3.73603959e-262, 6.02658058e-154, 6.55490914e-260],  # may vary
       [5.30498948e-313, 3.14673309e-307, 1.00000000e+000]])


np.arange(10, 30, 5)
array([10, 15, 20, 25])
np.arange(0, 2, 0.3)  # it accepts float arguments
array([0., 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])

np.arange(10, 30, 5)
array([10, 15, 20, 25])
np.arange(0, 2, 0.3)  # it accepts float arguments
array([0., 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
