#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 24 / 09 / 2024
# Program Menghitung rumus balok

# Menghitung keliling balok menggunakan lambda
keliling_balok = lambda p, l, t: 4 * (p + l + t)
luas_permukaan_balok = lambda p, l, t: 2 * (p * l + p * t + l * t)

# Function untuk menampilkan hasil
def hitung_balok(p, l, t):
    keliling = keliling_balok(p, l, t)
    luas = luas_permukaan_balok(p, l, t)
    return f"Keliling balok: {keliling:.2f}, Luas permukaan balok: {luas:.2f}"

# Input panjang, lebar, dan tinggi balok
p = float(input("Masukkan panjang balok: "))
l = float(input("Masukkan lebar balok: "))
t = float(input("Masukkan tinggi balok: "))

# Output hasil perhitungan
print(hitung_balok(p, l, t))