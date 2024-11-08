#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menghitung Jarak

print("\033[1;34m=====================")
print("====PERPINDAHAN LEBUR ES====")
print("=========================\n")

m = int(input("Masukan berat/massa benda: "))
c = (2100)
suhu1 = int(input("Masukan Suhu Pertama: "))
suhu2 = int(input("Masukan Suhu Kedua: "))
dt = (suhu2 - suhu1)
l = 336000
ca = 4200

q1 = m * c * dt
q2 = m * l 
q3 = m * ca * dt

print("\033[95m================================")
print("===KALOR JENIS ES====")
print("\033[95m===============================")
print(f"Jadi kalor jenis es : {round(q1,2)} J\n")
print("\033[91m================================")
print("====KALOR LEBUR ES====")
print("==============================")
print(f"Jadi Kalor Lebur Es = {round(q2, 2)} J\n")
print("\033[92m================================")
print("===KALOR JENIS AIR====")
print("======================================")
print(f"Jadi Kalor Jenis Air = {round(q3, 2)} J\n")
print("\033[92m==============================")