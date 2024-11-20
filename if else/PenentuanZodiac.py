# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Penentuan Zodiak Berdasarkan Bulan

print("="*40)
print("Program Penentu Zodiak Berdasarkan Bulan")
print("="*40)
bulan = int(input("Masukkan bulan (1-12): "))

if bulan == 1:
    print("Zodiak: Capricorn atau Aquarius")
elif bulan == 2:
    print("Zodiak: Aquarius atau Pisces")
elif bulan == 3:
    print("Zodiak: Pisces atau Aries")
elif bulan == 4:
    print("Zodiak: Aries atau Taurus")
elif bulan == 5:
    print("Zodiak: Taurus atau Gemini")
elif bulan == 6:
    print("Zodiak: Gemini atau Cancer")
elif bulan == 7:
    print("Zodiak: Cancer atau Leo")
elif bulan == 8:
    print("Zodiak: Leo atau Virgo")
elif bulan == 9:
    print("Zodiak: Virgo atau Libra")
elif bulan == 10:
    print("Zodiak: Libra atau Scorpio")
elif bulan == 11:
    print("Zodiak: Scorpio atau Sagittarius")
elif bulan == 12:
    print("Zodiak: Sagittarius atau Capricorn")
else:
    print("Bulan tidak valid.")
print("="*40)