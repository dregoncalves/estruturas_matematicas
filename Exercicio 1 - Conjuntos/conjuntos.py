from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Definindo dois conjuntos
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Plotando o diagrama de Venn
venn2([A, B], ('Conjunto A', 'Conjunto B'))
plt.title('Diagrama de Venn de Dois Conjuntos')
plt.show()