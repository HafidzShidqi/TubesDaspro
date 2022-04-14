from fungsi import *
import time

def buy_game(user, dataGame, dataUser, dataKepemilikan, dataRiwayat):
    idGame = input("Masukkan ID Game: ")

    valid = True
    if not idGame:
        print("\nInputan tidak valid!")
    elif Length(dataGame)-1 < getIndexID(idGame):
        print("\nTidak ada Game dengan ID tersebut!\n")

    else:
        for i in range(1, Length(dataKepemilikan)):
            if dataKepemilikan[i][0] == idGame and dataKepemilikan[i][1] == user:
                valid =  False
        
        if valid == False:
            print("\nAnda sudah memiliki Game tersebut!\n")


        else:
            if int(dataGame[getIndexID(idGame)][-1]) == 0 :
                print("\nStok Game tersebut sedang habis!\n")
    

            elif int(dataUser[getIndexID(user)][-1]) < int(dataGame[getIndexID(idGame)][4]):
                print("\nSaldo anda tidak cukup untuk membeli Game tersebut!\n")
    

            else:
                stokAwal = int(dataGame[getIndexID(idGame)][-1])
                dataGame[getIndexID(idGame)][-1] = str(stokAwal -1)

                saldoAwal = int(dataUser[getIndexID(user)][-1])
                dataUser[getIndexID(user)][-1] = str(saldoAwal - int(dataGame[getIndexID(idGame)][4]))

                dataKepemilikan = append(dataKepemilikan, [[idGame, user]])

                dataRiwayat = append(dataRiwayat, [[idGame, dataGame[getIndexID(idGame)][1], dataGame[getIndexID(idGame)][4], user, str(time.gmtime().tm_year)]])

                print(f'\nGame "{dataGame[getIndexID(idGame)][1]}" berhasil dibeli!\n')

    return dataGame, dataUser, dataKepemilikan, dataRiwayat

    


