import matplotlib.pyplot as plt
import numpy as np

def plot_function(start, end, step, color, linestyle, marker, label):
    x_values = np.arange(start, end + step, step)
    y_values = x_values ** 3

    plt.plot(x_values, y_values, color=color, linestyle=linestyle, marker=marker, label=label)

start = -2
end = 2

# Построение графиков с разными параметрами
plot_function(start, end, 0.01, color='blue', linestyle='-', marker='o', label='Step 0.01')
plot_function(start, end, 0.1, color='orange', linestyle='--', marker='x', label='Step 0.1')
plot_function(start, end, 0.25, color='green', linestyle=':', marker='s', label='Step 0.25')

# Настройка графика
plt.title('График функции $x^3$')
plt.xlabel('x')
plt.ylabel('$x^3$')
plt.legend()
plt.grid(True)

# Сохранение графика в различных форматах
plt.savefig('graph.pdf', format='pdf', bbox_inches='tight')
plt.savefig('graph.png', format='png', bbox_inches='tight')
plt.savefig('graph.svg', format='svg', bbox_inches='tight')

plt.show()
