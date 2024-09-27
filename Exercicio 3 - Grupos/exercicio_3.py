import matplotlib.pyplot as plt
import numpy as np

# Vamos ilustrar a operação de adição em Z (inteiros)
x = np.arange(-5, 6)
y = x + 2

plt.stem(x, y, basefmt=" ")  # Remover o argumento 'use_line_collection'
plt.title("Grupo: Inteiros com a adição")
plt.show()