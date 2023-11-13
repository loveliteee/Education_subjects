import matplotlib.pyplot as plt
import numpy as np

# Определение функции
def func(x, y):
    return x**2 - y**2

# Создание данных
x_values = np.linspace(-3, 3, 100)
y_values = np.linspace(-3, 3, 100)
x_mesh, y_mesh = np.meshgrid(x_values, y_values)
z_values = func(x_mesh, y_mesh)

# Построение закрашенной контурной диаграммы
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
contour_plot = plt.contourf(x_mesh, y_mesh, z_values, cmap='viridis')
plt.colorbar(contour_plot, label='Значения функции')
plt.title('Закрашенная контурная диаграмма')
plt.xlabel('x')
plt.ylabel('y')

# Построение трехмерного графика
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_surface(x_mesh, y_mesh, z_values, cmap='viridis', alpha=0.8)
ax.set_title('Трехмерный график')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
