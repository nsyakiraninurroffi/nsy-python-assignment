#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menghitung Diskon Bersadarkan Total Belanja

print("Program Menghitung Diskon Berdasarkan Total Belanja")
def hitung_diskon(total_belanja):
    if total_belanja >= 100000:
        return total_belanja * 0.1
    return 0

print("="*40)
total_belanja = float(input("Masukkan total belanja: "))
diskon = hitung_diskon(total_belanja)
total_bayar = total_belanja - diskon
print(f"Total yang harus dibayar: {total_bayar}")
print("="*40)