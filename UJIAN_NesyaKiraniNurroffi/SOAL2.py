#SOAL
#Tampilkan tanggal sekarang seperti format berikut:
#Wednesday, 13 of September on 2023, 08:42:34 AM

# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 19 / 11 / 2024
# Program Ujian soal 2

from datetime import datetime

sekarang = datetime.now()
format_data = sekarang.strftime("%A, %d of %B on %Y, %I:%M:%S %p")
print(format_data)
