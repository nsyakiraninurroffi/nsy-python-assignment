#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 20 / 11 / 2024
# Program mengonversi jarak dari sentimeter (cm) ke kilometer (km), meter (m), dan sentimeter (cm)

import os
os.system("cls")
def konversi_jarak(x):  
    
    km = x // 100000  
    sisa_cm = x % 100000  
    m = sisa_cm // 100 
    cm = sisa_cm % 100  

    return km, m, cm  

x = 261341  
km, m, cm = konversi_jarak(x)  

print(f"{km} km + {m} m + {cm} cm")