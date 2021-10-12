"""
Nama: Gagah Putra Bangsa
Program: Menghitung total biaya pengiriman
Dibuat tanggal 05 Oktober 2021
"""
import sys


count=0
print("Daftar Hotkey\nj->Jabodetabek\ndj->Pulau Jawa\nlj->Luar Jawab")
while count==0:
    i= {"q","j","dj","lj"}

    tujuan= input("Tujuan Barang(q-quit)= ")
    if tujuan=="q":
        sys.exit(0)
    elif tujuan == "j":
        print("Jabodetabek")
        harga= 10000
    elif tujuan == "dj":
        print("Dalam Pulau Jawa")
        harga= 25000
    elif tujuan == "lj":
        print("Luar pulau Jawa")
        harga=50000
    else:
        print ("Invalid input")
        tujuan= input("tujuan barang= ")
# memasukan kembali variabel untuk perintah if !=i 
    j = harga = 10000
    dj = harga = 25000
    lj = harga = 50000
# meminta input dari user untuk berat barang    
    berat = int(input("Berat Barang = "))
    if berat <= 20:
        n = 15000
    elif berat > 20:
        n = 15000 +((berat-20)*1500)
    
    while berat < 1:
        print("Tidak Valid, masukan kembali")
        berat = int(input("Berat Barang = "))
    if berat > 20:
        n = 15000 +((berat-20)*1500)



    

    print("------------Rincian Biaya-----------")
    print("1.tujuan=",tujuan,"","","","","","","","harga= Rp.",harga)
    print("2.Berat=",berat,"kg","","","","harga= Rp.",n)
    print("3.PPN 10%=                Rp.",int(harga+n)*(10/100))
    print("4.Total=                  Rp.",harga+n+int(harga+n)*(10/100))
    print("-------------------------------------")