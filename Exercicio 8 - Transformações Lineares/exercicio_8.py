import matplotlib.pyplot as plt
import numpy as np

theta = np.radians(45)  # ângulo de 45 graus
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], 
                            [np.sin(theta), np.cos(theta)]])

# Vetor original
vector = np.array([1, 0])

# Rotacionando o vetor
rotated_vector = rotation_matrix @ vector

# Gráfico
plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='r', label="Vetor Original")
plt.quiver(0, 0, rotated_vector[0], rotated_vector[1], angles='xy', scale_units='xy', scale=1, color='b', label="Vetor Rotacionado (45º)")
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.title("Rotação de um Vetor em 45º")
plt.show()
