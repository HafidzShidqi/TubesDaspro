from fungsi import Length, isNum

def topup(dataUser):
    username = input("Masukan username: ")
    saldo = input("Masukan saldo: ")
    
    valid1 = False
    index = 0
    if isNum(saldo) == False:
        print("\nError! Mohon masukkan saldo yang benar (berupa integer)!\n")
    else:
        saldo = int(saldo)
        for i in range(1,Length(dataUser)):
            if dataUser[i][1] == username:
                index = i
                valid1 = True
                break

        saldoAwal = int(dataUser[i][-1])

        if saldoAwal + saldo < 0:
            valid2 = False
        else:
            valid2 = True
        
        if valid1 ==  False:
            print(f'\nUsername "{username}" tidak ditemukan.\n')
        elif valid2 ==  False:
            print(f"\nTidak bisa mengurangi saldo karena saldo {dataUser[i][1]} adalah {dataUser[i][-1]} < {saldo*-1} \n")
        elif valid1 == valid2 == True:
            dataUser[index][-1] = str(saldoAwal + saldo)
            if saldo > 0:
                print(f"\nTop up berhasil. Saldo {dataUser[index][2]} bertambah menjadi {dataUser[index][-1]}.\n")
            elif saldo < 0:
                print(f"\nTop up berhasil. Saldo {dataUser[index][2]} berkurang menjadi {dataUser[index][-1]}.\n")
            else:
                print(f"\nTop up berhasil. Saldo {dataUser[index][2]} tetap menjadi {dataUser[index][-1]}.\n")
    return dataUser


