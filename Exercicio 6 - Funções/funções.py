import matplotlib.pyplot as plt
import numpy as np

# Definindo a função f(x) = x^3
def f(x):
    return x**3

# Valores para x
x = np.linspace(-2, 2, 100)
y = f(x)

# Plotar a função
plt.plot(x, y, label='f(x) = x^3')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Gráfico de f(x) = x^3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()