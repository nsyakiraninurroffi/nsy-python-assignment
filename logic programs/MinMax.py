import os
os.system ("cls")

a = int(input("Masukan angka ke 1: "))
b = int(input("Masukan angka ke 2: "))
c = int(input("Masukan angka ke 3: "))

print("Angka terkecil: ",min(a,b,c)) 
print("Angka terbesar: ",max(a,b,c))

if min(a,b,c) and max(a,b,c): 
    kali = min(a,b,c)*2 
    print("Angka", min(a,b,c), "Dikalikan dengan dua: ",kali) 
    bagi = max(a,b,c)/2
    print("Angka", max(a,b,c), "Dibagikan dengan dua: ",bagi)