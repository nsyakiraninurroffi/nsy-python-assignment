#SOAL
#Tuliskan sebuah program python untuk menentukan apakah suatu inputan angka termasuk ratusan, ribuan, atau jutaan

# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 19 / 11 / 2024
# Program Ujian soal 8

def kategori_angka(angka):  
    if angka >= 1000000:  
        return "Jutaan"  
    elif angka >= 1000:  
        return "Ribuan"  
    elif angka >= 100:  
        return "Ratusan"  
    else:  
        return "Kurang dari 100"  
 
try:
    input_angka = int(input("Masukkan sebuah angka: "))  
    kategori = kategori_angka(input_angka)  
    print(f"Angka {input_angka} termasuk dalam kategori: {kategori}")  
except ValueError:  
    print("Silakan masukkan angka yang valid.")
