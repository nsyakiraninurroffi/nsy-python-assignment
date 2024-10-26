#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 26 / 10 / 2024
# Program Konversi Durasi Waktu


# Input durasi dalam detik
print("="*40)
durasi_detik = int(input("Masukkan durasi dalam detik: "))

# Mengonversi ke hari, jam, menit, dan detik
hari = durasi_detik // (24 * 3600)
durasi_detik %= (24 * 3600)
jam = durasi_detik // 3600
durasi_detik %= 3600
menit = durasi_detik // 60
detik = durasi_detik % 60

# Menampilkan hasil konversi
print(f"{hari} hari, {jam} jam, {menit} menit, {detik} detik")
print("="*40)