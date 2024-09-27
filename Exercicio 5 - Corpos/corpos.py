import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Elementos do corpo finito GF(4)
elements = ['0', '1', 'a', 'a+1']

# Matriz de multiplicação para GF(4)
gf_multiplication = np.array([
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [0, 2, 3, 1],
    [0, 3, 1, 2]
])

# Criação de uma matriz 4x4 com os nomes dos elementos
annot_matrix = np.array([
    ['0', '0', '0', '0'],
    ['0', '1', 'a', 'a+1'],
    ['0', 'a', 'a+1', '1'],
    ['0', 'a+1', '1', 'a']
])

# Visualizar a matriz de multiplicação com anotação correta
plt.figure(figsize=(6, 4))
sns.heatmap(gf_multiplication, annot=annot_matrix, fmt="", cmap='coolwarm', cbar=False)
plt.title('Tabela de Multiplicação para GF(4)')
plt.xlabel('Elemento')
plt.ylabel('Elemento')
plt.show()