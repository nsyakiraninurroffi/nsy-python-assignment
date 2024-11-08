# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menghitung Kalor Jenis Air

print('\n')
print('='*40)
print('Menghitung kalor jenis es')
print('='*40)

massa = int(input('\033[93mMasukan massa\t\t: '))
suhu2 = int(input('\033[93mMasukan suhu kedua\t: '))
suhu1 = int(input('\033[93mMasukan suhu pertama\t: '))
print("="*40)

Q = massa * 4200 * (suhu2-suhu1)

print(f'\n\033[32mKalor jenis air\t\t: {round (Q,2)}J\n')
print("="*40)