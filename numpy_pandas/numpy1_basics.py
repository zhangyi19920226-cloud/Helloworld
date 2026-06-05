import numpy as np

angles = np.array([0, np.pi/6, np.pi/4, np.pi/2, np.pi])
print(np.sin(angles))  # 计算angles数组中每个元素的正弦值
print(np.cos(angles))  # 计算angles数组中每个元素的余弦值

x = np.array([0, 1, 2, 3])
print(np.exp(x))

print(np.sqrt(np.array([1, 4, 9, 16])))
print(np.log(np.array([1, np.e, np.e**2])))

