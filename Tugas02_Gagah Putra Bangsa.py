"""
Nama: Gagah Putra Bangsa
Program: Menghitung total biaya pengiriman
Dibuat tanggal 05 Oktober 2021
"""
import sys


count=0
print("Daftar Hotkey\nj->Jabodetabek\ndj->Pulau Jawa\nlj->Luar Jawab")
while count==0:
    
    tujuan= input("Tujuan Barang(q-quit)= ")
    if tujuan=="q":
        sys.exit(0)
    elif tujuan == "j":
        harga= 10000
    elif tujuan == "dj":
        harga= 25000
    elif tujuan == "lj":
        harga=50000
    else:
        print ("Invalid input")
        tujuan= input("tujuan barang= ")
                
    berat = int(input("Berat Barang = "))
    if berat <= 20:
        n = 15000
    elif berat > 20:
        n = berat * 1500
        ppn = (harga+n)/10

    print("------------Rincian Biaya-----------")
    print("1.tujuan= ",tujuan,     "harga= Rp.",harga)
    print("2.Berat=  ",berat,"kg", "harga= Rp.",n)
    print("3.PPN 10%= Rp.", ppn)
    print("4.Total= Rp.",harga+n+ppn)
    print("-------------------------------------")