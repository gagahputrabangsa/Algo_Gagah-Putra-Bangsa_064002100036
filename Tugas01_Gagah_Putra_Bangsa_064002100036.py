"""
program    : Mengubah format tanggal
dibuat oleh: Gagah Putra Bangsa - 064002100036
Tanggal dev: 28/09/2021

program ini mengubah format tanggal, bulan dan tahun dari yang seperti 28/09/2021 
menjadi seperti 28-Sep-2021
"""


#memasukan data yang diperlukan untuk proses input
data = {"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr",
	     "05":"Mei", "06":"Jun", "07":"Jul", "08":"Agt",
	     "09":"Sep", "10":"Okt", "11":"Nov", "12":"Des"}
#memasukan perintah yang akan ditampilkan di layar
input1 = input("masukkan tanggalnya dd/mm/yyyy: ")
#memasukan perintah split() agar memperingati user jika ada kesalahan dalam memasukan suatu input
input1 = input1.split("/")
#memproses hasil yang diinput oleh user
hasil = f'{input1[0]}-{data[f"{input1[1]}"]}-{input1[2]}'
#menampilkan hasil yang sudah di proses oleh user
print(hasil)
print("sekian dari saya terimakasih")