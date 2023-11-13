import matplotlib.pyplot as plt
import numpy as np

# Функции степенных многочленов
def polynomial_function(x, degree):
    return x ** degree

# Функции синусоид
def sinusoidal_function(t, frequency):
    return np.sin(2 * np.pi * frequency * t)

# Функции синусоид с начальными фазами
def phased_sinusoidal_function(t, phase):
    return np.sin(2 * np.pi * t + phase)

# Логарифмические функции
def logarithmic_functions(x):
    return np.log2(x), np.log(x), np.log10(x)

# Гиперболические функции
def hyperbolic_functions(x):
    return np.sinh(x), np.cosh(x), np.tanh(x)

# Создание массива значений для оси x
x_values = np.linspace(-1, 1, 1000)

# Создание подграфиков
fig, axes = plt.subplots(3, 3, figsize=(15, 15))
fig.suptitle('Семейство функций', fontsize=16)

# Построение графиков для степенных многочленов
for degree, ax in zip(range(1, 7), axes[0]):
    ax.plot(x_values, polynomial_function(x_values, degree), label=f'Degree {degree}')
    ax.set_title(f'Degree {degree}')
    ax.grid(True)
    ax.legend()

# Построение графиков для синусоид
for frequency, ax in zip(range(2, 9), axes[1]):
    ax.plot(x_values, sinusoidal_function(x_values, frequency), label=f'Frequency {frequency}')
    ax.set_title(f'Frequency {frequency}')
    ax.grid(True)
    ax.legend()

# Построение графиков для синусоид с начальными фазами
for phase, ax in zip(np.linspace(0, 5 * np.pi / 6, 6), axes[2]):
    ax.plot(x_values, phased_sinusoidal_function(x_values, phase), label=f'Phase {phase:.2f}')
    ax.set_title(f'Phase {phase:.2f}')
    ax.grid(True)
    ax.legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Построение графиков в различных конфигурациях
configurations = [(1, 1), (1, 2), (1, 3), (2, 2)]
titles = ['1 столбец', '2 столбца', '3 столбца', '1 строка']

for config, title in zip(configurations, titles):
    fig, axes = plt.subplots(config[0], config[1], figsize=(15, 5))
    fig.suptitle(title, fontsize=16)
    
    # Построение графиков для степенных многочленов
    for degree, ax in zip(range(1, 7), axes):
        ax.plot(x_values, polynomial_function(x_values, degree), label=f'Degree {degree}')
        ax.set_title(f'Degree {degree}')
        ax.grid(True)
        ax.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Автоматическое сохранение графиков
for degree in range(1, 7):
    plt.plot(x_values, polynomial_function(x_values, degree), label=f'Degree {degree}')
plt.title('Степенные многочлены')
plt.legend()
plt.grid(True)
plt.savefig('polynomial_functions.png')
plt.savefig('polynomial_functions.pdf')
plt.savefig('polynomial_functions.svg')
plt.show()

# Круговая диаграмма
labels = ['Одни пятёрки', 'Пятёрки и четвёрки', 'С тройками, без задолженностей', 'С задолженностями, пересдали', 'Несдавшие и отчисленные']
sizes = [15, 30, 20, 10, 5]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Студенты группы по итогам сессии')
plt.show()
