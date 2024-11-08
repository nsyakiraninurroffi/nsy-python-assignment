# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Cek Bilangan Prima

print("="*40)
angka = int(input("Masukkan sebuah angka: "))

if angka > 1:
    for i in range(2, angka):
        if (angka % i) == 0:
            print("Itu Bukan bilangan prima ish.")
            break
    else:
        print("Yup Itu Bilangan prima.")
else:
    print("Itu Bukan bilangan prima ish.")
print("="*40)
