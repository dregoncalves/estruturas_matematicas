import matplotlib.pyplot as plt
import numpy as np


# Representação gráfica de uma função no plano cartesiano
x = np.linspace(-10, 10, 400)
y = x**2

plt.plot(x, y, label="y = x^2")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Plano Cartesiano")
plt.legend()
plt.grid(True)
plt.show()