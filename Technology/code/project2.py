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

# Построение графика для степенных многочленов
plt.subplot(3, 3, 1)
for degree in range(1, 7):
    plt.plot(x_values, polynomial_function(x_values, degree), label=f'Degree {degree}')
plt.title('Степенные многочлены')
plt.legend()

# Построение графика для синусоид
plt.subplot(3, 3, 2)
for frequency in range(2, 9):
    plt.plot(x_values, sinusoidal_function(x_values, frequency), label=f'Frequency {frequency}')
plt.title('Синусоиды')

# Построение графика для синусоид с начальными фазами
plt.subplot(3, 3, 3)
for phase in np.linspace(0, 5 * np.pi / 6, 6):
    plt.plot(x_values, phased_sinusoidal_function(x_values, phase), label=f'Phase {phase:.2f}')
plt.title('Синусоиды с начальными фазами')
plt.legend()

# Построение графика для логарифмических функций
plt.subplot(3, 3, 4)
for func, label in zip(logarithmic_functions(x_values), ['log2(x)', 'ln(x)', 'log10(x)']):
    plt.plot(x_values, func, label=label)
plt.title('Логарифмические функции')
plt.legend()

# Построение графика для гиперболических функций
plt.subplot(3, 3, 5)
for func, label in zip(hyperbolic_functions(x_values), ['sh(x)', 'ch(x)', 'th(x)']):
    plt.plot(x_values, func, label=label)
plt.title('Гиперболические функции')
plt.legend()

plt.tight_layout()
plt.show()
