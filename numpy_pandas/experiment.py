import numpy as np
import math
B = np.arange(3)
B
np.exp(B)
print(np.exp(B))  # 计算B数组中每个元素的指数值，即e的B数组中每个元素次幂
print(np.sqrt(B))
print(math.exp(2))


a = np.arange(10)**3
a
a[2]  # 取出a数组中索引为2的元素
a[2:5]  # 取出a数组中索引从2到5（不包含5）的元素
a[0:6:2]  # 取出a数组中索引从0到6（不包含6），步长为2的元素
# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000
a[:6:2] = 1000  # equivalent to a[0:6:2] = 1000;# 从开始到位置6（不包含6），步长为2，将每个元素设置为1000
a
a[::-1]  # 反转数组，步长为-1表示从后向前取元素
for i in a:
    print(i**(1 / 3.))


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
b
print(b[2, 3])  # 取出b数组中第3行第4列的元素（索引从0开始）索引为2的行和索引为3的列
print(b[0:5, 1])  # 取出b数组中索引从0到5（不包含5）的行和索引为1的列的元素，即第2列的所有元素
print(b[:, 1])    # equivalent to the previous example
print(b[1:3, :])  # each column in the second and third row of b
