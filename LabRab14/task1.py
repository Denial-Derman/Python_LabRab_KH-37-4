import numpy as np
import matplotlib.pyplot as plt

#Y(x)=5*sin(10*x)*sin(3*x), x=[0...4]
# Визначення функції
x = np.linspace(0, 4, 500)
y = 5 * np.sin(10 * x) * np.sin(3 * x)

# Побудува графіка функції
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='#FF4500', linewidth=1.5, linestyle='-', label=r"$Y(x)=5\sin(10x)\sin(3x)$")

# Додавання міток, заголовок та легенду
plt.xlabel("x", fontsize=12)
plt.ylabel("Y(x)", fontsize=12)
plt.title("Графік функції Y(x)", fontsize=14)
plt.legend(fontsize=12)

# Відобразити сітку та графік
plt.grid(alpha=0.6)
plt.show()
