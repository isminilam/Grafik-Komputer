import matplotlib.pyplot as plt
import numpy as np

# Parameter lingkaran
r = 5      # jari-jari lingkaran
a, b = 10, 6  # titik pusat lingkaran (a, b)

# Menghasilkan koordinat lingkaran
theta = np.linspace(0, 2 * np.pi, 100)  # Membuat 100 nilai theta dari 0 hingga 2π
x = a + r * np.cos(theta) # Menghitung titik-titik x untuk membentuk lingkaran
y = b + r * np.sin(theta) # Menghitung titik-titik y untuk membentuk lingkaran

# Plot lingkaran
plt.figure(figsize=(6,6))   # Membuat grafik dengan ukuran 6x6
plt.plot(x, y, label=f'Lingkaran dengan r={r}') # Menggambar lingkaran berdasarkan nilai x dan y yang dihitung
plt.xlabel('x') # Memberi label pada sumbu x
plt.ylabel('y') # Memberi label pada sumbu y
plt.axhline(0, color='black', linewidth=0.5) # Membuat garis horizontal di sumbu y = 0
plt.axvline(0, color='black', linewidth=0.5) # Membuat garis horizontal di sumbu x = 0
plt.scatter(a, b, color='red', label='Pusat Lingkaran') # Menandai titik pusat lingkaran pada koordinat (a, b)

plt.gca().set_aspect('equal', adjustable='box') # agar sumbu x dan y memiliki skala yang sama
plt.title('Persamaan Lingkaran') # Judul
plt.legend(loc='upper left') # Menampilkan legenda di pojok kiri atas
plt.grid() # Menambahkan grid pada grafik
plt.show() # Menampilkan grafik
