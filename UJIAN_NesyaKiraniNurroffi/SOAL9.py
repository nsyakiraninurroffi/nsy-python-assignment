#SOAL
#Buatlah program python dengan inputan 2 angka, apabila angka ke 2 adalah dua kali lipat dari
#angka ke 1, maka dikalikan 3 angka pertama, apabila tidak jumlahkan ke dua angka tersebut!

# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 19 / 11 / 2024
# Program Ujian soal 9

a = int(input('Masukkan Angka Pertama : '))
b = int(input('Masukkan Angka Kedua : '))

c = a*a

if b == c :
    print (b*a*a*a)
else:
    print (a+b)