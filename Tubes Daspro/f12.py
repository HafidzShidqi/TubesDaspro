from fungsi import Length, isNum

def topup(dataUser):
    # Procedure topup (input dataUser: array)
	# Prosedur untuk menambahkan saldo pada user yang diminta sesuai input
	# I.S pengguna memasukan username dan tambahan saldo yang diinginkan
	# F.S nominal saldo pengguna bertambah
	
    # KAMUS
	# Username, dataUser[i][1] : string
	# Saldo, dataUser[i][-1], index, i : integer
	# Valid1, valid2 = boolean

    # ALGORIIMA
    # input
    username = input("Masukan username: ")
    saldo = input("Masukan saldo: ")
    
    # deklarasi variabel
    valid1 = False
    index = 0
    if isNum(saldo) == False:   # pengecekan apakah saldo valid
        print("\nError! Mohon masukkan saldo yang benar (berupa integer)!\n")
    else:
        saldo = int(saldo)  # penyesuaian user jika saldo valid
        for i in range(1,Length(dataUser)):
            if dataUser[i][1] == username:
                index = i
                valid1 = True
                break

        saldoAwal = int(dataUser[i][-1])    # deklarasi saldo awal

         # pengondisian output berdasarkan input
        if saldoAwal + saldo < 0:   # jika jumlah total  <0
            valid2 = False
        else:
            valid2 = True   # jika jumlah total >0
        
        if valid1 ==  False:    # jika username tidak valid/tidak ditemukan
            print(f'\nUsername "{username}" tidak ditemukan.\n')
        elif valid2 ==  False:  # jika jumlah total <0
            print(f"\nTidak bisa mengurangi saldo karena saldo {dataUser[i][1]} adalah {dataUser[i][-1]} < {saldo*-1} \n")
        elif valid1 == valid2 == True:
            dataUser[index][-1] = str(saldoAwal + saldo)
            if saldo > 0:
                print(f"\nTop up berhasil. Saldo {dataUser[index][2]} bertambah menjadi {dataUser[index][-1]}.\n")  # jika taransaksi berhasil dan jumlah saldo bertambah
            elif saldo < 0:
                print(f"\nTop up berhasil. Saldo {dataUser[index][2]} berkurang menjadi {dataUser[index][-1]}.\n")  # jika taransaksi berhasil dan jumlah saldo berkurang
            else:
                print(f"\nTop up berhasil. Saldo {dataUser[index][2]} tetap menjadi {dataUser[index][-1]}.\n") # jika taransaksi berhasil dan jumlah saldo tetap
    return dataUser


