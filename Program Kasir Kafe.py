import os
os.system('clear')

# projek = " Kafe Sistem Informasi C "
# tp = 50

# print(f"\n{projek.title().center(tp,'-')}")
# pembeli = input("\nNama Pembeli\t\t: ")
#print("Nama Pembeli\t\t: ",pembeli.title())


#-------------- MENU MAKANAN --------------
def makanan():
    global totalmkn
    global porsi
    global mkn
    global menan
    menan = " menu makanan "
    print(f"""
1.Bakso ---------------- Rp. 10000
2.Mie Ayam ------------- Rp. 15000
3.Soto ----------------- Rp. 12000
4.Nasi Goreng ---------- Rp. 15000
5.Ayam Geprek ---------- Rp. 10000
0.Skip Makanan""")
    nomor = int(input("Masukan Nomor Pilihan\t: "))
    porsi = int(input("Berapa Porsi\t\t: "))
    if porsi<=0:
        print("Porsi Tidak Boleh Negatif, Silahkan Isi Porsi")
        makanan()
    elif nomor==1:
        totalmkn = porsi*10000
        print(porsi," Porsi Bakso\t\t: Rp.",totalmkn)
        mkn = ("Bakso")
    elif nomor==2:
        totalmkn = porsi*15000
        print(porsi," Porsi Mie Ayam\t: Rp.",totalmkn)
        mkn = ("Mie Ayam")
    elif nomor==3:
        totalmkn = porsi*12000
        print(porsi," Porsi Soto\t\t: Rp.",totalmkn)
        mkn = ("Soto")
    elif nomor==4:
        totalmkn = porsi*15000
        print(porsi," Porsi Nasi Goreng\t: Rp.",totalmkn)
        mkn = ("Nasi Goreng")
    elif nomor==5:
        totalmkn = porsi*10000
        print(porsi," Porsi Ayam Geprek\t: Rp.",totalmkn)
        mkn = ("Ayam Geprek")
    elif nomor==0:
        totalmkn = porsi*0
        print("Tidak Memesan Makanan")
        mkn = ("Makanan --")
    else:
        print("Pilihan tidak ada, silahkan pilih Menu lain ")
        makanan()


#-------------- MENU MINUMAN --------------
def minuman():
    global totalmnm
    global mnm
    global gelas
    global menum
    menum = " menu minuman "
    print(f"""
1.Air Mineral ---------- Rp. 1000
2.Es Teh --------------- Rp. 4000
3.ES Jeruk ------------- Rp. 6000
4.Es Kopi -------------- Rp. 5000
5.Teh Hangat ----------- Rp. 4000
0.Skip Minuman """)
    nomor = int(input("Masukan Nomor Pilihan\t: "))
    gelas = int(input("Berapa Gelas\t\t: "))
    if gelas <=0:
        print("Gelas Tidak Boleh Negatif, Silahkan Isi Gelas")
        minuman()
    elif nomor==1:
        totalmnm = gelas*1000
        print(gelas," Air Mineral\t\t: Rp.",totalmnm)
        mnm = ("Air Mineral")
    elif nomor==2:
        totalmnm = gelas*4000
        print(gelas," Es Teh Manis\t\t: Rp.",totalmnm)
        mnm = ("Es Teh")
    elif nomor==3:
        totalmnm = gelas*6000
        print(gelas," Es Jeruk\t\t: Rp.",totalmnm)
        mnm = ("Es Jeruk")
    elif nomor==4:
        totalmnm = gelas*5000
        print(gelas," Es Kopi\t\t: Rp.",totalmnm)
        mnm = ("Es Kopi")
    elif nomor==5:
        totalmnm = gelas*4000
        print(gelas," Es Teh Hangat\t: Rp.",totalmnm)
        mnm = ("Teh Hangat")
    elif nomor==0:
        totalmnm = gelas*0
        print("Tidak Memesan Minuman")
        mnm = ("Minuman --")
    else:
        print("Pilihan tidak ada, silahkan pilih Menu lain ")
        minuman()

#-------------- STRUK PESANAN --------------
def bayar():
    total = totalmkn+totalmnm
    struk = " PESANAN "
    print("\nTotal harus Dibayar\t: Rp.",total)
    uang = int(input("Uang Tunai Pembeli\t: Rp. "))

    if uang >= total:
        print(f"\n{struk.upper().center(tp,'=')}")
        print("-"*tp)
        print(f"\nNama\t\t\t: {pembeli.title()}")
        print(f"Pesanan\t\t\t: {porsi} {mkn} Rp.{totalmkn}")
        print(f"\t\t\t  {gelas} {mnm} Rp.{totalmnm}")
        print(f"Total\t\t\t: Rp.{uang}")
        kembalian = int(uang-total)
        print(f"Kembalian\t\t: Rp.{kembalian}\n")
        print("-"*tp)
        print("="*tp)
        print()
    else:
        if uang < 0:
            print("Uang Tunai TIdak Boleh Negatif!!")
            bayar()
        else:
            uang <= total
            maaf = " Mohon Maaf Uang Kamu Gak Cukup :( "
            print(f"\n{maaf.title().center(tp,'-')}")
            bayar()


def main():
    global pembeli
    global tp
    projek = " Kafe Sistem Informasi C "
    tp = 50

    while True:
        print(f"\n{projek.title().center(tp, '-')}")
        pembeli = input("\nNama Pembeli\t\t: ")

        makanan()
        minuman()
        bayar()

        ulang = input("Apakah Anda ingin memesan lagi? (y/n): ").lower()
        if ulang != 'y':
            print("Terima kasih atas pesanannya. Sampai jumpa!")
            break
        else:
            main()

if __name__ == "__main__":
    main()