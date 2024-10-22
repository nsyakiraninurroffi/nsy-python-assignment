#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 24 / 09 / 2024
# Program Menghitung rumus bola

import math

# Menghitung keliling lingkaran besar bola menggunakan lambda
keliling_bola = lambda r: 2 * math.pi * r
luas_permukaan_bola = lambda r: 4 * math.pi * r ** 2

# Function untuk menampilkan hasil
def hitung_bola(r):
    keliling = keliling_bola(r)
    luas = luas_permukaan_bola(r)
    return f"Keliling lingkaran besar bola: {keliling:.2f}, Luas permukaan bola: {luas:.2f}"

# Input jari-jari bola
r = float(input("Masukkan jari-jari bola: "))

# Output hasil perhitungan
print(hitung_bola(r))