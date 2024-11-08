#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menentukan Cuaca Bersdasarkan Suhu

print("="*40)
print("Program Menentukan Cuaca Berdasarkan Suhu Celcius")
print("="*40)
suhu = float(input("Masukkan suhu saat ini (°C): "))

if suhu >= 30:
    print("Cuaca panas.")
elif suhu >= 20:
    print("Cuaca hangat.")
elif suhu >= 10:
    print("Cuaca dingin.")
else:
    print("Cuaca sangat dingin.")

print("="*40)