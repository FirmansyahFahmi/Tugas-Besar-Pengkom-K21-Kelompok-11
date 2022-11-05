# Kamus
# Simpan_Saldo   = Menyimpan nilai dari nominal saldo e-money ditambah dengan tarif total   : int
# Cash1          = Nominal pembayaran cash                                                  : int

import os
import time

def Tol_Tutup(): # Fungsi untuk output pintu tol tertutup
    os.system('cls')
    print("""














||=======||
||==   ==||*********************************************
||== T ==||*********************************************
||== O ==||
||== L ==||
||==   ==||
||=======||
||=======||


""")

def Tol_Buka(x, y, z): # Fungsi untuk output pintu tol terbuka, golongan, tarif, dan saldo
    time.sleep(0.2)
    os.system('cls')
    x -= y
    print("""
           ***
           ***
           ***
           ***
           ***
           ***
           ***
           ***
           ***
           ***
           ***
           ***
           ***
           ***
||=======||***
||==   ==||***
||== T ==||***
||== O ==||
||== L ==||
||==   ==||
||=======||
||=======||


""")
    print("Golongan: " + str(z))
    print("Tarif   : Rp " + str(y))
    print("Saldo   : Rp " + str(x))
        
Tol_Tutup()

Berat = float(input("Berat (ton): ")) # input berat mobil
Roda = int(input("Roda       : ")) # input banyak roda mobil
Jarak = float(input("Jarak  (Km): "))   # input jarak dari pintu tol masuk ke pintu tol keluar
Cash2 = 0 # deklarasi Cash2

Tol_Tutup()

if (Berat <= 5 and Roda <= 6): # Jika berat <= 5 ton dan roda <= 6, maka termasuk golongan I dengan tarif golongan Rp 5000
    Golongan = 1
    Tarif_Golongan = 5000
elif (Berat <= 10 and Roda <= 6): # Jika berat <= 10 ton dan roda <= 6, maka termasuk golongan II dengan tarif golongan Rp 10000
    Golongan = 2
    Tarif_Golongan = 10000
elif (Berat <= 20 and Roda <= 10): # Jika berat <= 20 ton dan roda <= 10, maka termasuk golongan III dengan tarif golongan Rp 15000
    Golongan = 3
    Tarif_Golongan = 15000
elif (Berat <= 30 and Roda <= 14): # Jika berat <= 30 ton dan roda <= 14, maka termasuk golongan IV dengan tarif golongan Rp 20000
    Golongan = 4
    Tarif_Golongan = 20000
else: # Jika berat > 30 ton dan roda > 14, maka termasuk golongan V dengan tarif golongan Rp 25000
    Golongan = 5 
    Tarif_Golongan = 25000

Tarif_Total = Tarif_Golongan + (Jarak * 1000) # Menghitung tarif total, yaitu dengan menambah tarif golongan dengan jarak * Rp 1000
print("Tarif Tol Rp " + str(int(Tarif_Total)))
Saldo = int(input("Saldo (Rp) : ")) # input saldo e-money

if (Saldo < Tarif_Total): # Jika saldo e-money kurang dari tarif total
    Tol_Tutup()
    print("""
Maaf saldo Anda tidak mencukupi.
Silahkan keluar dari pintu paling kanan dan pilih 2 opsi berikut:
1. Top Up Saldo E-Money
2. Pembayaran Cash
""")
    case = int(input()) # Input case

    match case: 
        case 1: # Jika memilih opsi 1. Top up saldo e-money
            while (Saldo < Tarif_Total): # Jika saldo e-money kurang dari tarif total
                Tol_Tutup()
                print("Mininal Nominal Top Up Saldo E-Money adalah Rp " + str(int(Tarif_Total) -  Saldo) + ".")
                Top_Up = int(input("Berapa nominal Top Up Saldo E-Money (Rp): ")) # input nominal top up saldo e-money
                Saldo += Top_Up # Saldo ditambah dengan nominal top up saldo e-money
            Tol_Buka (Saldo, int(Tarif_Total), Golongan)
        case 2: # Jika memilih opsi 2. Pembayaran cash
            Simpan_Saldo = Saldo + int(Tarif_Total) # deklarasi Simpan_Saldo dengan nominal saldo e-money ditambah dengan tarif total
            while (Cash2 < Tarif_Total): # Jika pembayaran cash < tarif total
                Tol_Tutup()
                print("Pembayaran cash sebesar Rp " + str(int(Tarif_Total - Cash2)))
                Cash1 = int(input("Cash (Rp): ")) # input nominal pembayaran cash
                Cash2 += Cash1 # Nominal cash ditambah dengan nominal pembayaran cash
            Tol_Buka(Simpan_Saldo, int(Tarif_Total), Golongan)
            if (Cash2 > Tarif_Total): # Jika nominal cash > tarif total, maka ada kembalian
                print("Kembali : Rp " + str(int(Cash2 - Tarif_Total)))
else: # Jika saldo e-money >= tarif total
    Tol_Buka(Saldo, int(Tarif_Total), Golongan)

print("""


||=======================================================||
||                                                       ||
|| Terima Kasih dan Selamat Melanjutkan Perjalanan Anda. ||
||                                                       ||
||=======================================================||


""")