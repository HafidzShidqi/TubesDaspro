from fungsi import *
import time

def buy_game(user, dataGame, dataUser, dataKepemilikan, dataRiwayat):
    # Procedure buy_game(input user, input/output dataGame, input/output dataUser, input/output dataKepemilikan, input/output dataRiwayat) 
    # {Prosedur untuk membeli game dari toko 
    # I.S user, dataGame, dataUser, dataKepemilikan, dataRiwayat terdefinisi 
    # F.S stok awal game dari dataGame berkurang, saldo user dari dataUser berkurang, dan 
    # game yang dibeli ditambahkan ke dataKepemilikan dan dataRiwayat} 
    
    # KAMUS LOKAL
    # idGame : string
    # valid : boolean
    # i,j, stokAwal, saldoAwal : integer 

    # ALGORITMA
    idGame = input("Masukkan ID Game: ")

    valid = True
    if not idGame:
        # Input kosong
        print("\nInputan tidak valid!")
    elif Length(dataGame)-1 < getIndexID(idGame):
        # ID tidak yang diinginkan tidak ada
        print("\nTidak ada Game dengan ID tersebut!\n")

    else:
        # Cek apakah game sudah dimiliki user
        for i in range(1, Length(dataKepemilikan)):
            if dataKepemilikan[i][0] == idGame and dataKepemilikan[i][1] == user:
                valid =  False
        
        if valid == False:
            # Game sudah dimiliki user
            print("\nAnda sudah memiliki Game tersebut!\n")


        else:
            # Cek apakah stok game cukup
            if int(dataGame[getIndexID(idGame)][-1]) == 0 :
                print("\nStok Game tersebut sedang habis!\n")
    
            # Cek apakah saldo user cukup
            elif int(dataUser[getIndexID(user)][-1]) < int(dataGame[getIndexID(idGame)][4]):
                print("\nSaldo anda tidak cukup untuk membeli Game tersebut!\n")
    

            else: # Pembelian valid
                # Kurangi stok game yang bersangkutan
                stokAwal = int(dataGame[getIndexID(idGame)][-1])
                dataGame[getIndexID(idGame)][-1] = str(stokAwal -1)

                # Kurangi saldo user
                saldoAwal = int(dataUser[getIndexID(user)][-1])
                dataUser[getIndexID(user)][-1] = str(saldoAwal - int(dataGame[getIndexID(idGame)][4]))
                
                # Tambahkan game ke dataKepemilikan dan dataRiwayat
                dataKepemilikan = append(dataKepemilikan, [[idGame, user]])
                dataRiwayat = append(dataRiwayat, [[idGame, dataGame[getIndexID(idGame)][1], dataGame[getIndexID(idGame)][4], user, str(time.gmtime().tm_year)]])
                
                # Tampilkan pesan pembelian berhasil
                print(f'\nGame "{dataGame[getIndexID(idGame)][1]}" berhasil dibeli!\n')

    return dataGame, dataUser, dataKepemilikan, dataRiwayat

    


