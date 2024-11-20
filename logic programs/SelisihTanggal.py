#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 20 / 11 / 2024
# Program Menghitung Selisih Tanggal

import os
os.system ("cls")
def hitung_total_hari(hari, bulan, tahun):
    return (tahun * 365) + (bulan * 30) + hari


hari1, bulan1, tahun1 = map(int, input("Masukkan tanggal pertama (dd:mm:yy): ").split(":"))
hari2, bulan2, tahun2 = map(int, input("Masukkan tanggal kedua (dd:mm:yy): ").split(":"))

total_hari1 = hitung_total_hari(hari1, bulan1, tahun1)
total_hari2 = hitung_total_hari(hari2, bulan2, tahun2)
selisih_hari = abs(total_hari2 - total_hari1)

tahun = selisih_hari // 365
sisa_hari = selisih_hari % 365
bulan = sisa_hari // 30
hari = sisa_hari % 30

# Output hasil
print(f"Selisih antara kedua tanggal adalah {tahun} tahun, {bulan} bulan, {hari} hari.")
