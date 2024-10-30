import matplotlib.pyplot as plt
import numpy as np

# Parameter lingkaran
r = 5      # jari-jari lingkaran
a, b = 10, 6  # titik pusat lingkaran (a, b)

# Menghasilkan koordinat lingkaran
theta = np.linspace(0, 2 * np.pi, 100)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)

# Plot lingkaran
plt.figure(figsize=(6,6))
plt.plot(x, y, label=f'Lingkaran dengan r={r}')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter(a, b, color='red', label='Pusat Lingkaran')

# Menambahkan rumus lingkaran di dalam grafik
equation = f"(x - {a})² + (y - {b})² = {r*r}"
plt.text(a - 8, b + 2, equation, fontsize=12, color='blue')  # Posisi teks disesuaikan

plt.gca().set_aspect('equal', adjustable='box')
plt.title('Persamaan Lingkaran')
plt.legend(loc='upper left')
plt.grid()
plt.show()
