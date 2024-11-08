#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Cek Kelebihan Berat Badan

print("="*40)
print("PROGRAM CEK KELEBIHAN BERAT BADAN")
print("="*40)
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))
print("="*40)

bmi = berat / (tinggi ** 2)

if bmi < 18.5:
    print("Berat Badan Kamu Kurang!")
elif bmi < 24.9:
    print("Berat Badan Kamu Normal!")
elif bmi < 29.9:
    print("kamu Kelebihan Berat Badan!")
else:
    print("kamu Mengalami Obesitas!")

print("="*40)