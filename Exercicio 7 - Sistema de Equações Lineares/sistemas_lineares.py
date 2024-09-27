import matplotlib.pyplot as plt
import numpy as np

# Coeficientes do sistema
a1, b1, c1 = 1, 2, 3   # x + 2y = 3
a2, b2, c2 = 2, -1, 1  # 2x - y = 1
a3, b3, c3 = -1, 1, 2  # -x + y = 2  

# Linhas do sistema
x = np.linspace(-5, 5, 100)
y1 = (c1 - a1 * x) / b1
y2 = (c2 - a2 * x) / b2
y3 = (c3 - a3 * x) / b3  

plt.plot(x, y1, label=f'{a1}x + {b1}y = {c1}')
plt.plot(x, y2, label=f'{a2}x - {b2}y = {c2}')
plt.plot(x, y3, label=f'{a3}x + {b3}y = {c3}') 

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Sistema Linear de 3 Equações')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.show()
