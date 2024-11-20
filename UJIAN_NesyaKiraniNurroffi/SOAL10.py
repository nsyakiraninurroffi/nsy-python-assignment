#SOAL
# Buatlah program python untuk memasukkan kalimat yang ditandai tanda 
# akhir kalimat bisa titik, tanda tanya, atau tanda seru. 
# Apabila kata pertama tidak ada kata apakah maka tambahkan apakah, dan apabila tanda di akhir bukan tanda tanya 
# maka tambahkan tanda tanya.

# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 19 / 11 / 2024
# Program Ujian soal 10

def proses_kalimat(kalimat):  
    kalimat = kalimat.strip()  

    if kalimat.endswith('.'):  
        kalimat = kalimat[:-1] 
    elif kalimat.endswith('!'):  
        kalimat = kalimat[:-1]    
    if not kalimat.lower().startswith("apakah"):  
        kalimat = "Apakah " + kalimat     
    kalimat += '?'  

    return kalimat   
input_kalimat = input("Masukkan kalimat: ")  
output_kalimat = proses_kalimat(input_kalimat)  
print("Output:", output_kalimat)