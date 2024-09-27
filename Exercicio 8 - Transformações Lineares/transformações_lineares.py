import matplotlib.pyplot as plt
import numpy as np

# Definindo a transformação linear
A = np.array([[2, 0], [0, 1]])  # Escala x por 2 e y permanece o mesmo

# Vetores antes e depois da transformação
vectors = np.array([[1, 0], [0, 1]])  # Vetores base
transformed_vectors = A @ vectors.T  

plt.quiver([0, 0], [0, 0], vectors[:, 0], vectors[:, 1], color=['r', 'b'], scale=1, scale_units='xy', angles='xy')
plt.quiver([0, 0], [0, 0], transformed_vectors[0], transformed_vectors[1], color=['r', 'b'], linestyle='--', scale=1, scale_units='xy', angles='xy')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Transformação Linear: A @ [1, 0] e [0, 1]')
plt.grid()
plt.gca().set_aspect('equal')
plt.show()