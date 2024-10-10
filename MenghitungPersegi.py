# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 24 / 09 / 2024
# Program Menghitung rumus persegi
def persegi():
    sisi = int(input("Masukan Sisi\t\t\t:  "))
    luas = lambda s : s * s 
    keliling = lambda s : 4 * s
    
    print("Luas Persegi Adalah\t\t: ", luas(sisi), "cm2")
    print("Keliling Persegi Adalah\t\t: ", keliling(sisi), "cm")
    print('='*40)
    
persegi()
persegi()
persegi()