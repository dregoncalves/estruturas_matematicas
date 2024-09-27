import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Matriz de adição para o anel Z/4Z
Z4_addition = np.array([[ (i+j) % 4 for j in range(4)] for i in range(4)])

# Visualizar a matriz de adição
plt.figure(figsize=(6, 4))
sns.heatmap(Z4_addition, annot=True, cmap='coolwarm', cbar=False)
plt.title('Tabela de Adição para Z/4Z')
plt.xlabel('Elemento')
plt.ylabel('Elemento')
plt.show()