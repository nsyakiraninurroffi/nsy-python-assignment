#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 26 / 10 / 2024
# Program Konversi Hari

#INPUT JUMLAH HARI
print("="*40)
jumlah_hari = int(input("Masukan Jumlah Hari\t\t"))

#MENGONVERSI KE TAHUN, BULAN DAN HARI
tahun = jumlah_hari // 365
jumlah_hari %= 365
bulan = jumlah_hari // 30
hari = jumlah_hari % 30

#MENAMPILKAN HASIL KONVERSI
print(f"{tahun} tahun, {bulan} bulan, {hari} hari")
print("="*40)
