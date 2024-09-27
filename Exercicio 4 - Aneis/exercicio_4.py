import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-5, 6)
y = x * 3

plt.stem(x, y, basefmt=" ")
plt.title("Anel: Inteiros com a multiplicação")
plt.show()