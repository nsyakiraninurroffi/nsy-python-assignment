nilai = []
jumlah = int(input('Jumlah data yang akan di input : '))

for i in range(jumlah):
    nilai.append(int(input(f'Nilai ke-{i+1} : ')))

#perhitungan data di list 
total = max = 0
min = nilai[0]
for data in nilai:
    total += data
    if data > max :
        max = data

    if data < min :
        min = data


print(f"\ntotal")
print(f'Rata-rata : {total / jumlah}')
print(f'Nilai terbesar : {max}')
print(f'Nilai terkecil : {min}')