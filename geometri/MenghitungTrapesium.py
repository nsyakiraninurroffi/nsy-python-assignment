#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 24 / 09 / 2024
# Program Menghitung rumus jajar genjang

# Menghitung keliling trapesium menggunakan lambda
keliling_trapesium = lambda a, b, c, d: a + b + c + d
luas_trapesium = lambda a, b, t: 0.5 * (a + b) * t

# Function untuk menampilkan hasil
def hitung_trapesium(a, b, c, d, t):
    keliling = keliling_trapesium(a, b, c, d)
    luas = luas_trapesium(a, b, t)
    return f"Keliling trapesium: {keliling:.2f}, Luas trapesium: {luas:.2f}"

# Input panjang sisi sejajar (a dan b), sisi lainnya (c dan d), serta tinggi (t)
a = float(input("Masukkan panjang sisi sejajar a: "))
b = float(input("Masukkan panjang sisi sejajar b: "))
c = float(input("Masukkan panjang sisi c: "))
d = float(input("Masukkan panjang sisi d: "))
t = float(input("Masukkan tinggi trapesium: "))

# Output hasil perhitungan
print(hitung_trapesium(a, b, c, d, t))