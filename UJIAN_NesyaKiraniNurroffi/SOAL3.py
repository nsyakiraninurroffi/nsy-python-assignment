#SOAL
# Buatlah function mengembalikan nilai untuk menghitung rumus volume tabung (phi*r*t) 
# kemudian tampilkan hasilnya dengan tambahan satuan volume

# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 19 / 11 / 2024
# Program Ujian soal 3

import math
print("="*40)
def hitung_volume_tabung(jari_jari, tinggi):
    volume = math.pi * (jari_jari ** 2) * tinggi
    return volume

jari_jari = float(input("Masukan jari-jari tabung\t:"))
tinggi = float(input("Masukan tinngi tabung\t\t:"))

volume_tabung = hitung_volume_tabung(jari_jari, tinggi)
print(f"Volume Tabung Adalah\t\t: {volume_tabung:.2f} Satuan Kubik")
print("="*40)
