import matplotlib.pyplot as plt
import numpy as np

# Conjunto de frações racionais simples
fractions = np.array([1/1, 1/2, 1/3, 1/4, 1/5, 1/6])
multiplication_factor = 1/2  # Multiplicando todos os elementos por 1/2

# Aplicando a multiplicação no conjunto
result = fractions * multiplication_factor

# Configuração do gráfico
plt.plot(fractions, result, 'o-', label=f'Multiplicação por {multiplication_factor}')
plt.title("Corpo dos Números Racionais: Multiplicação por 1/2")
plt.xlabel("Frações Originais")
plt.ylabel("Resultado da Multiplicação")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()