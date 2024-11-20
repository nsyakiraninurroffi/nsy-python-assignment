#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 20 / 11 / 2024
# Program mempertukarkan tripel (x, y, z) menjadi (y, z, x)

import os
os.system ("cls")

print("="*40)
print("Program mempertukarkan tripel (x, y, z) menjadi (y, z, x)")
print("="*40)
x = int(input("Masukkan bilangan pertama (x): "))
y = int(input("Masukkan bilangan kedua (y): "))
z = int(input("Masukkan bilangan ketiga (z): "))

temp = x
x = y
y = z
z = temp

print(f"Setelah dipertukarkan: x = {x}, y = {y}, z = {z}")
print("="*40)
