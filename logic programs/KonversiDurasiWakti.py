# INPUT DURASI WAKTU DALAM DETIK
durasi_detik =int(input("Masukan Durasi Waktu Dalam Detik\t\t:"))

# MENGKONVERSI WAKTU DALAM HARI, JAM, MENIT DAN DETIK
hari = durasi_detik // (24 * 3600)
durasi_detik %= (24 * 3600)
jam = durasi_detik // 3600
durasi_detik %= 3600
menit = durasi_detik // 60
detik = durasi_detik % 60

#MENAMPILKAN HASIL KONVERSI
print(f'{hari} hari, {jam} jam, {menit} menit, {detik} detik')