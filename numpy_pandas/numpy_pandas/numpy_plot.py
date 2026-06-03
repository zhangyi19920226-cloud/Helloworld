import numpy as np
import matplotlib.pyplot as plt

# 生成 0 到 2π 的 1000 个点
x = np.linspace(0, 8 * np.pi, 1000)  # 生成从0到2π的1000个点，作为x轴数据

# 计算各函数值
y_sin = np.sin(x)
y_cos = np.cos(x)
y_exp = np.exp(x) / np.exp(x).max()  # 缩放到 0-1 方便对比

# 画图
plt.figure(figsize=(16, 4))  # 设置图像大小
plt.plot(x, y_sin, label="sin(x)", color="blue")  # 绘制sin(x)曲线，设置标签和颜色
plt.plot(x, y_cos, label="cos(x)", color="red")
plt.plot(x, y_exp, label="exp(x) normalized", color="green")

# 装饰
plt.title("NumPy Universal Functions")  # 设置图像标题
plt.xlabel("x")  # 设置x轴标签
plt.ylabel("y")  # 设置y轴标签
plt.legend()  # 显示图例
plt.grid(True)  # 显示网格
plt.axhline(0, color='black', linewidth=0.5)  # 添加水平线y=0

plt.show()  # 显示图像
