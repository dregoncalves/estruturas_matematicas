import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 400)
y = x**2

plt.plot(x, y, label="y = x^2")
plt.title("Função Quadrática")
plt.grid(True)
plt.legend()
plt.show()

# Representação de uma função exponencial
y_exp = np.exp(x/5)

plt.plot(x, y_exp, label="y = exp(x/5)")
plt.title("Função Exponencial")
plt.grid(True)
plt.legend()
plt.show()