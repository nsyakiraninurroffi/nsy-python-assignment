#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Login Gmail

import os
os.system ("cls")

USERNAME = 'nesyakiraninurroff@gmail.com'
PASSWORD = '12345678'

username = input("Masukan username\t : ")
password = input("Masukan password : ")

if username != USERNAME :
    print("username tidak tersedia." )
elif username == USERNAME and password != PASSWORD :
    print("Password salah!")
else :
    print("Selamat datang ",username)