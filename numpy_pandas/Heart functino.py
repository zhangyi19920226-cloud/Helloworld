import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 1000)
y = np.linspace(-3, 3, 1000)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

plt.contour(X, Y, Z, levels=[0], colors='green')  # 绘制Z=0的等高线，即心形轮廓
plt.title('Heart Shape Contour')
plt.xlabel('X-axis')  # 设置x轴标签
plt.ylabel('Y-axis')  # 设置y轴标签
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.axis('equal')
plt.grid(True)
plt.show()


