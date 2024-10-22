#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 24 / 09 / 2024
# Program Menghitung rumus limas segitiga

import math

# Menghitung keliling alas limas segitiga menggunakan lambda
keliling_alas_limas = lambda a, b, c: a + b + c

# Menghitung luas permukaan limas segitiga
# Luas permukaan limas segitiga = luas alas + luas sisi tegak (luas tiga segitiga)
luas_permukaan_limas = lambda a, b, c, t_alas, t_sisi1, t_sisi2, t_sisi3: (
    0.5 * a * t_alas + 0.5 * a * t_sisi1 + 0.5 * b * t_sisi2 + 0.5 * c * t_sisi3
)

# Function untuk menampilkan hasil
def hitung_limas(a, b, c, t_alas, t_sisi1, t_sisi2, t_sisi3):
    keliling = keliling_alas_limas(a, b, c)
    luas = luas_permukaan_limas(a, b, c, t_alas, t_sisi1, t_sisi2, t_sisi3)
    return f"Keliling alas limas: {keliling:.2f}, Luas permukaan limas: {luas:.2f}"

# Input panjang sisi-sisi alas, tinggi alas, dan tinggi sisi tegak limas
a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))
c = float(input("Masukkan panjang sisi c: "))
t_alas = float(input("Masukkan tinggi alas segitiga: "))
t_sisi1 = float(input("Masukkan tinggi sisi tegak pada sisi a: "))
t_sisi2 = float(input("Masukkan tinggi sisi tegak pada sisi b: "))
t_sisi3 = float(input("Masukkan tinggi sisi tegak pada sisi c: "))

# Output hasil perhitungan
print(hitung_limas(a, b, c, t_alas, t_sisi1, t_sisi2, t_sisi3))