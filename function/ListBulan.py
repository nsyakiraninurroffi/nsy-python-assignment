#ibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 26 / 10 / 2024
# Program Fuction List Bulan

print("="*40)
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "juni", "Juli",
        "Agustus", "September", "Oktober", "November", "Desember"]

print(bulan[2])
print(bulan[9])
bulan[7] = "August"
bulan[0] = "January"
bulan.append("Muharram")

for index, data in enumerate(bulan):
    print(f"bulan ke-{index+1} : {data}")
print("="*40) 