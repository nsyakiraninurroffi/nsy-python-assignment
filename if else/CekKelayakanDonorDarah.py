#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Cek Kelayakan Donor Darah


print("\033[1;32m="*40)
print("\033[1;34mPROGRAM CEK KELAYAKAN DONOR DARAH")
usia = int(input("\033[1;34mMasukkan usia Anda: "))
print("\033[1;32m="*40)
berat_badan = float(input("\033[1;34mMasukkan berat badan Anda (kg): "))
print("\033[1;32m="*40)
sehat = input("\033[1;34mApakah Anda dalam kondisi sehat? (ya/tidak): ").lower()
print("\033[1;32m="*40)

if usia >= 17 and usia <= 60 and berat_badan >= 50 and sehat == "ya":
    print("\033[1;36mAnda layak menjadi pendonor darah.")
else:
    print("\033[0;31mMaaf, Anda belum memenuhi syarat untuk mendonorkan darah.")
