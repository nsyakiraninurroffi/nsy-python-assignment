#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menentukan Jenis Segitiga

print("PROGRAMS MENENTUKAN JENIS SEGITIGA")
print("\033[1;34m="*40)
a = float(input("Masukkan sisi pertama: "))
b = float(input("Masukkan sisi kedua: "))
c = float(input("Masukkan sisi ketiga: "))

if a == b == c:
    print("Segitiga sama sisi.")
elif a == b or b == c or a == c:
    print("Segitiga sama kaki.")
else:
    print("Segitiga sembarang.")
print("\033[34m="*40)
