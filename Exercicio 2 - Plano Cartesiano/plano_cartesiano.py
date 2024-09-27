import matplotlib.pyplot as plt

# Pontos e linhas no plano cartesiano
x = [0, 1, 2, 3]
y = [1, 4, 9, 16]

# Plotar pontos
plt.scatter(x, y, color='red')
plt.plot(x, y, label='y = x^2')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Relações no Plano Cartesiano')
plt.legend()
plt.grid()
plt.show()