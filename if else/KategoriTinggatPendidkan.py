#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Program Menentukan Tingkat Pendidikan Sesuai Umur

print("="*40)
print("Program Menentukan Tingkat Pendidikan Sesuai Umur")
print("="*40)
usia = int(input("Masukkan usia Anda\t: "))
print("="*40)

if usia < 5:
    print("\033[0;31mAnda mungkin belum cukup umur untuk pendidikan formal.")
elif 5 <= usia <= 6:
    print("\033[0;33mAnda berada di usia Taman Kanak-Kanak (TK).")
elif 7 <= usia <= 12:
    print("Anda berada di usia Sekolah Dasar (SD).")
elif 13 <= usia <= 15:
    print("\033[0;34mAnda berada di usia Sekolah Menengah Pertama (SMP).")
elif 16 <= usia <= 18:
    print("\033[0;37mAnda berada di usia Sekolah Menengah Atas (SMA).")
else:
    print("\033[0;32mAnda mungkin berada di usia kuliah atau pendidikan lain.")

print("="*40)
