import matplotlib.pyplot as plt
import numpy as np

# Exemplo de um conjunto aberto (intervalo aberto de (0, 1))
x = np.linspace(0, 1, 100)
y = np.zeros_like(x)
plt.plot(x, y, 'o', label="Conjunto Aberto (0,1)")
plt.title("Representação de um Conjunto Aberto")
plt.legend()
plt.show()