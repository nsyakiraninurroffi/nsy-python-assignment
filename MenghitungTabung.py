#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 24 / 09 / 2024
# Program Menghitung rumus tabung

import math

# Menghitung keliling alas tabung (lingkaran) menggunakan lambda
keliling_alas_tabung = lambda r: 2 * math.pi * r
luas_alas_tabung = lambda r: math.pi * r ** 2

# Menghitung luas permukaan tabung
# Luas permukaan tabung = 2 * luas alas + keliling alas * tinggi
luas_permukaan_tabung = lambda r, t: 2 * luas_alas_tabung(r) + keliling_alas_tabung(r) * t

# Menghitung volume tabung
# Volume tabung = luas alas * tinggi
volume_tabung = lambda r, t: luas_alas_tabung(r) * t

# Function untuk menampilkan hasil
def hitung_tabung(r, t):
    luas_permukaan = luas_permukaan_tabung(r, t)
    volume = volume_tabung(r, t)
    return f"Luas permukaan tabung: {luas_permukaan:.2f}, Volume tabung: {volume:.2f}"

# Input jari-jari alas dan tinggi tabung
r = float(input("Masukkan jari-jari alas tabung: "))
t = float(input("Masukkan tinggi tabung: "))

# Output hasil perhitungan
print(hitung_tabung(r, t))