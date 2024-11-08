#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 26 / 10 / 2024
# Program Menentukan Grade Nilai


def tentukan_grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    elif nilai >= 60:
        return "D"
    return "E"

print("="*40)
nilai = int(input("Masukkan nilai: "))
print(f"Grade: {tentukan_grade(nilai)}")
print("="*40)