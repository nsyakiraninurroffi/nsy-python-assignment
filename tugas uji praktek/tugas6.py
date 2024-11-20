print("="*40)
nilai = int(input('Masukan Nilai Anda :'))

if nilai >= 85:
    hasil = "A"
elif nilai >= 70:
    hasil = "B"
elif nilai >= 60:
    hasil = "C"
else:
    hasil = "D"
    
print("Nilai Kamu : ", hasil,)
print("="*40)