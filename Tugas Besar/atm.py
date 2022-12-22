import os

os.system('cls' or 'clear')
user_id = 0
loop = "n"
users = [
    {
        "id": "1234",
        "no_rekening": "222104012",
        "username": "ADITWN",
        "pin": "222222",
        "saldo": 42000000
    },
    {
        "id": "4321",
        "no_rekening": "222104011",
        "username": "IRFAN",
        "pin": "111111",
        "saldo": 67000000
    },
    {
        "id": "5678",
        "no_rekening": "222104004",
        "username": "HANDARU",
        "pin": "444444",
        "saldo": 80000000
    }
]
status_login = False
pakai_atm = "y"
 
 
def cek_login(p):
    for user in users:
        if user['pin'] == p:
            return user
    return False
 
 
def cek_user(id):
    for i in range(len(users)):
        if users[i]['id'] == str(id):
            return int(i)
    return -1
 
 
def cek_rekening(no):
    for i in range(len(users)):
        if str(users[i]['no_rekening']) == str(no):
            return int(i)
    return -1
 
 
def tranfer_uang(uang, no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            users[index2]['saldo'] = users[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp." + str(uang) + " ke Rekening " + no_rekening)
            print("sisa saldo anda adalah Rp.", users[index1]['saldo'])
        else:
            print("Saldo anda tidak mencukupi")
 
 
def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            print("Anda berhasil menarik uang Rp." + str(uang))
            print("sisa saldo anda adalah Rp.", users[index1]['saldo'])
        else:
            print("Saldo anda tidak mencukupi")
 
 
while pakai_atm == "y":
    while not status_login:
        print("            ===============================================")
        print("             SELAMAT DATANG DI ATM BANK Pesonainformatika")
        print("            ===============================================")
        print('\n')
        print('\n')
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN : ")
 
        cl = cek_login(pin)
        if cl:
            os.system('cls' or 'clear')
            print("selamat datang " + cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            os.system('cls' or 'clear')
            print("")
            print("PIN yang anda masukkan salah")
            print("")

 
    while loop == "y" and status_login:
        os.system('cls' or 'clear')
        print("                              HALO  " + cl['username'])
        user_id = cl['id']
        status_login = True
        loop = "y"
        u = users[cek_user(user_id)]
        print("            ===============================================")
        print("             SELAMAT DATANG DI ATM BANK Pesonainformatika")
        print("            ===============================================")
        print('\n')
       
        print("1. Cek Saldo")
        print("2. Transfer Uang")
        print("3. Ambil Uang")
        print("4. Logout")
        print("5. Keluar ATM")
        print('\n')
        a = int(input("Silahkan pilih jenis transaksi : "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.", u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            os.system('cls' or 'clear')
            print("===================================")
            print("Silahkan Masukan No Rekening Tujuan")  
            print("===================================")
            print("") 
            print("") 
            print("") 
            no_rek = input("Masukan No Rekening Tujuan    : ")
            
            cnk = cek_rekening(no_rek)
 
            if cnk == 1 or 2:
                nominal = int(input("Nominal Yang Akan Di Transfer : Rp. "))
                print("")
                print("")
                yorn = input('Apakah anda ingin melajutkan? (Y/N) : ')
                if yorn == ('y' or 'Y'):
                    os.system('cls' or 'clear')
                    nama = cek_user(id)
                    saldo = u['saldo']
                    sisa_saldo = saldo - nominal
                    print('     INFORMASI TRANSAKSI')
                    print('')
                    print(f"No Rekening : {no_rek}")
                    print(f"Nama        : {str(nama)}")
                    print(f'JUMLAH      : Rp. {nominal}')
                    print(f'Sisa Saldo  : Rp.',sisa_saldo)
                    
                    menu = input('Lanjut transaksi lainnya? (Y/N) : ')
                    if menu == ('y' or 'Y'):
                        break
                    else:
                        print('terimakasih')
                        status_login = False
                        loop = 'n'
                        pakai_atm = 'n'
                    #if no_rek == 222104011:
                        #print('Irfan Dwi Kurniadi')
                        #tranfer_uang(nominal, no_rek)
                        #print("")
                        #loop = "n"
                else:
                    print("")
                    print('kembali ke menu utama')
                    break
                
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"
 
        elif a == 3:
            os.system('cls' or 'clear')
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            os.system('cls' or 'clear')
            status_login = False
 
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
            print("")
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"
