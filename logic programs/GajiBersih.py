#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 26 / 10 / 2024
# Program Gaji Bersih

print('\n')
print('='*40)
print('Menentukan gaji bersih karyawan')
print('='*40)

karyawan = input('\nMasukan nama karywan\t\t: ')
gaji_pokok = int(input('Masukan gaji pokok karyawan\t: '))

tunjangan = int(0.2 * gaji_pokok)
pajak = int(0.15 * (gaji_pokok + tunjangan))

gaji_bersih = int((gaji_pokok + tunjangan) - pajak)

print("="*40)
print(f'''
gaji pokok : Rp.{gaji_pokok}
tunjangan  : Rp.{tunjangan}
pajak      : Rp.{pajak}
gaji bersih: Rp.{gaji_bersih}
\n''')
print("="*40)