#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menentukan Bilangan Positif, Negatif, atau Nol 

print("="*40)
print ("Program Menentukan Bilangan")
def cek_bilangan(angka):
    if angka > 0:
        return "positif"
    elif angka < 0:
        return "negatif"
    return "nol"

print("="*40)
angka = int(input("Masukkan angka: "))
print(f"{angka} adalah bilangan {cek_bilangan(angka)}.")
print("="*40)


