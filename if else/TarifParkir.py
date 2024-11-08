#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menghitung Tarif Parkir Per-jam

print("="*40)
print("Program Menghitung Tarif Parkir Per-jam")
print("="*40)
jam_parkir = int(input("Berapa jam Anda parkir? "))
print("="*40)

if jam_parkir <= 1:
    tarif = 5000
else:
    tarif = 5000 + (jam_parkir - 1) * 3000

print(f"Tarif parkir yang harus dibayar: Rp {tarif}")
print("="*40)