import os

os.system('clear')
def judul_1():
    print('==============================')
    print('Program ATM Bersama')
    print('==============================')
    print('\n')

judul_1()
username = int(input('Masukkan pin anda : '))



def func():  # ------->>> BAGIAN BODY
    os.system('clear')
    pilihan = [
        'Keluar',
        'Penarikan',
        'Transfer',
        'Pembayaran',
        'Ubah PIN',
        'Lihat Saldo',
    ]
    while True:
        
        def pilihan1():
            print('''           ----PILIH TRANSAKSI YANG ANDA INGINKAN---- 
              ----PILIH CANCEL UNTUK MEMBATALKAN----''')

            print('\n')
            for i,o in enumerate(pilihan) :
                print(i,'<---',o)
                #print('\n')

            print('\n')
            print('91 >> lainnya')
            print('\n')

        pilihan1()
        masukkan = int(input('pilih : '))
        if masukkan == 91:
            os.system('clear')
            pilihan2 = [
                'a',
                'b',
                'c',
                'd',
                'e',
                'f',
                'g',
                'h',
                'i',
            ]
            print('''           ----PILIH TRANSAKSI YANG ANDA INGINKAN---- 
              ----PILIH CANCEL UNTUK MEMBATALKAN----''')

            print('\n')
            for i,o in enumerate(pilihan2) :
                print(i,'<---',o)
                #print('\n')

            print('\n')
            print('12 << kembali')
            masukkan1 = int(input('pilih : '))
            if masukkan1 == 12:
                os.system('clear')
                continue
            
        elif masukkan == 0:
            os.system('clear')  
            print('\n')   
            print('Mengeluarkan kartu ....')
            print('\n')
            break
        elif masukkan == 1 :
            os.system('clear')
            print('''         ---SILAHKAN PILIH JUMLAH UANG---
             ATAU TRANSAKSI LAINNYA''')
            
            print('\n')
            jumlah = [
                '= 300.000',
                '= 500.000',
                '= 1.000.000',
                '= 1.500.000',
                '= 2.000.000',

            ]
            for i,o in enumerate(jumlah):
                print(i,o)
                print('\n')
            print('23 Transaksi Lainnya >>')
            print('\n')
            penarikan = int(input('Pilih : '))
            print('\n')
            if penarikan == 23:
                os.system('clear')
                continue

            elif penarikan == 0: #----------- RUMUS MTK
                os.system('clear')
                print('---PILIH DARI REKENING---')
                print('1. Rekening Giro')
                print('2. Rekening Tabungan')

                rekening = int(input('Pilih : '))

                pass
                

        elif masukkan == 2:
            os.system('clear')
            print('bagian tarik tunai') # isi tarik tunai
            print('\n')
            ils = input('Lanjut transaksi? (Y/N) : ')
            if ils == 'Y'or'y': #udah bener
                os.system('clear')
                continue    
            elif ils == 'n' or 'N':
                exit

        else:
            pass

if username == 1 : # ------->>> BAGIAN BODY
    os.system('clear')
    func()
else:
    for i in range(0,4):
        os.system('clear')
        judul_1()

        i -= 3 
        print(f'Sisa percobaan : {i}')
        username = int(input('Masukkan pin anda : '))
        if username == 1:
            func()
        elif i == -1:
            os.system('clear')
            print('\n\n')
            
            print('Kartu anda telah diblokir')
            print('Silahkan menghubungi cabang bank terdekat ')
            print('\n')
            break
     