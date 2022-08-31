# see https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300

resolution = 200

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


x = np.linspace(-6, 6, resolution)
y = np.linspace(-6, 6, resolution)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_title('surface');

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
fig.show()
