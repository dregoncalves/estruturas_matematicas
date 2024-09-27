import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 400)
y1 = 2*x + 1
y2 = -x + 5
y3 = 0.5*x - 2

plt.plot(x, y1, label="2x + y = 1")
plt.plot(x, y2, label="-x + y = 5")
plt.plot(x, y3, label="0.5x + y = -2")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Sistema de Equações Lineares")
plt.legend()
plt.grid(True)
plt.show()