
"""
Nama: Gagah Putra Bangsa
Program: Menghitung total biaya pengiriman
Dibuat tanggal 05 Oktober 2021
"""
def start() :
    print("Daftar Hotkey\nj-Jabodetabek\ndj-Pulau Jawa\nlj-Luar Jawab")
    tujuan= input("Tujuan Barang(q-quit)= ")

    if tujuan=="q":
                exit(0)
    berat = int(input("Berat Barang = "))
    if tujuan == "j":
        harga= 10000
    elif tujuan == "dj":
        harga= 25000
    elif tujuan == "lj":
        harga=50000
    else:
        print ("Invalid input")
        tujuan= input("tujuan barang= ")
        
    if berat <= 20:
        n = 15000
    elif berat > 20:
        n = berat * 1500

    ppn = (harga+n)/10

    print("------------Rincian Biaya-----------")
    print("1.tujuan= ",tujuan,     "harga= Rp.",harga)
    print("2.Berat=  ",berat,"kg", "harga= Rp.",n)
    print("3.PPN 10%= Rp.", ppn)
    print("4. Total= Rp.",harga+n+ppn)
    print("-------------------------------------")
    start()

start()