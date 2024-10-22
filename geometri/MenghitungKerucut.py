#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 24 / 09 / 2024
# Program Menghitung rumus kerucut

import math

# Menghitung keliling alas kerucut menggunakan lambda
keliling_alas_kerucut = lambda r: 2 * math.pi * r
luas_permukaan_kerucut = lambda r, s: math.pi * r * (r + s)

# Function untuk menampilkan hasil
def hitung_kerucut(r, s):
    keliling = keliling_alas_kerucut(r)
    luas = luas_permukaan_kerucut(r, s)
    return f"Keliling alas kerucut: {keliling:.2f}, Luas permukaan kerucut: {luas:.2f}"

# Input jari-jari alas (r) dan panjang garis pelukis (s)
r = float(input("Masukkan jari-jari alas kerucut: "))
s = float(input("Masukkan panjang garis pelukis kerucut: "))

# Output hasil perhitungan
print(hitung_kerucut(r, s))
print(hitung_kerucut(r, s))