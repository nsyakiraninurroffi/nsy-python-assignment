#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menghitung Panjang Teropong

print("\033[97m=============================")
print("MENGHITUNG PANJANG TEROPONG")
print("====================================")

fob =int(input("\033[1;35m Masukan Nilai Lensa Objektif: "))
fp =int(input("Masukan Nilai Lensa Pembalik: "))
fok =int(input("Masukan Nilai Lensa Okuler: "))

d = fob + (4*fp) + fok

print(f"\n\033[93m Panjang Teropong = {round (d, 2)}")

print("\033[97m=================================")