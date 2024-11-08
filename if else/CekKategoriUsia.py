# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Cek Kategori Usia

print("="*40)
print("PROGRAM CEK KATEGORI USIA")
usia = int(input("Masukkan usia Anda\t: "))
print("="*40)

if usia < 13:
    print("Kategori\t\t: Anak-anak")
elif usia < 18:
    print("Kategori\t\t: Remaja")
elif usia < 60:
    print("Kategori\t\t: Dewasa")
else:
    print("Kategori\t\t: Lansia")
print("="*40)