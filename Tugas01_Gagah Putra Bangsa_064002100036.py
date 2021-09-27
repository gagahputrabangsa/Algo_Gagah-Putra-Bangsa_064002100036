import datetime                                    #mengimport library
from datetime import timedelta                     #mengimport library

nah = input('Masukan tanggal format yyyy/mm/dd: ') #meminta input dari user
tanggal, bulan, tahun = map(int, nah.split('/'))   #menggunakan fungsi split untuk memisahkan tanggal,bulan,tahun
hasil = datetime.date(tanggal, bulan, tahun)       #memproses tanggal, bulan, tahun yang diinput user
print(f"Menjadi seperti ini : {hasil:%d-%b-%Y}")   #menampilkan hasil dengan format %d-%b-%Y

print("=========================================")
print("Nama: Gagah Putra Bangsa")
print("Nim : 064002100036")