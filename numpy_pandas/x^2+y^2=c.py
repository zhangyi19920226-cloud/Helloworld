import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.linspace(-2*np.pi, 2*np.pi, 1000)
x, y = np.meshgrid(x, y)
z = np.sin(x)**2 + y**2

plt.contour(x, y, z, levels=[1], colors='brown')
plt.title('Contour of Double Square Function')
plt.xlabel('x-direction')
plt.ylabel('y-direction')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.show()
