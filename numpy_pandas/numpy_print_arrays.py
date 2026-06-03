import numpy as np

a = np.arange(6)                    # 1d array
print(a)
b = np.arange(12).reshape(4, 3)     # 2d array  从0-11的整数中创建一个4行3列的二维数组
print(b)
c = np.arange(24).reshape(2, 3, 4)  # 3d array  从0-23的整数中创建一个2层3行4列的三维数组
print(c)

sys = __import__("sys")
np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported

a = np.array([20, 30, 40, 50])
b = np.arange(4)
b
c = a - b
c
b**2  # 元素级别的平方
10 * np.sin(a)  # 元素级别的正弦值乘以10
a < 35  # 元素级别的比较，返回一个布尔数组

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(A * B)     # elementwise product #逐元素乘积
print(A @ B)     # matrix product #矩阵乘积
print(A.dot(B))  # another matrix product

# create instance of default random number generator
rg = np.random.default_rng(1)
a = np.ones((2, 3), dtype=int)  # 创建一个以1填充的2行3列的整数数组
b = rg.random((2, 3))  # 创建一个2行3列的数组，元素是从均匀分布[0,1)中随机生成的浮点数
a *= 3  # 整数数组a中的每个元素乘以3
a
b += a  # 浮点数组b中的每个元素加上整数数组a中的对应元素，结果存储在b中。由于a是整数类型，而b是浮点类型，NumPy会自动将a转换为浮点类型以进行计算。这种类型转换称为广播（broadcasting）。
b
a += b  # b is not automatically converted to integer type

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)  # 创建一个包含3个元素的数组，这些元素在0和π之间均匀分布
b.dtype.name
'float64'
c = a + b
c
array([1., 2.57079633, 4.14159265])
c.dtype.name
'float64'
# 计算c数组中每个元素乘以虚数单位1j的指数值，结果是一个复数数组。对于每个元素x，计算公式为exp(x * 1j)，其中exp是自然指数函数，1j表示虚数单位。
d = np.exp(c * 1j)
d
array([0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
d.dtype.name
'complex128'  # 复数类型，表示实部和虚部都是64位浮点数的复数。

a = rg.random((2, 3))
a
a.sum()  # 计算数组a中所有元素的总和
a.min()  # 计算数组a中所有元素的最小值
a.max()  # 计算数组a中所有元素的最大值
a.mean()  # 计算数组a中所有元素的平均值
a.std()  # 计算数组a中所有元素的标准差
a.var()  # 计算数组a中所有元素的方差

b = np.arange(12).reshape(3, 4)
b
b.sum(axis=0)     # 按行方向计算，即把每一列的数相加 → [12,15,18,21]
b.min(axis=1)     # 按列方向计算，即找出每一行的最小值 → [0,4,8]
b.cumsum(axis=0)  # 按行方向计算累积和，即把每一列的数依次相加 → [[0,1,2,3],[4
# 按列方向计算累积和，即把每一行的数依次相加 → [[0,1,3,6],[4,9,15,22],[8,17,27,38]]
b.cumsum(axis=1)


# Universal functions
B = np.arange(3)
B
print(np.exp(B))  # 计算B数组中每个元素的指数值，即e的B数组中每个元素次幂
print(np.sqrt(B))  # 计算B数组中每个元素的平方根
print(np.add(B, B))  # 计算B数组中每个元素与自身相加的结果，即B数组中每个元素的两倍
C = np.array([2., -1., 4.])  # 创建一个包含三个元素的数组，分别是2.0、-1.0和4.0
np.add(B, C)  # 计算B数组中每个元素与C数组中对应元素相加的结果，返回一个新的数组。由于B是整数类型，而C是浮点类型，NumPy会自动将B转换为浮点类型以进行计算。这种类型转换称为广播（broadcasting）。结果是一个包含三个元素的数组，分别是2.0、0.0和7.0。
