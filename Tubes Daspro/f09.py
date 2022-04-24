from fungsi import *

def list_game(user, dataKepemilikan, dataGame):
    # procedure list_game(input dataKepemilikan, input dataGame : array, input user) 
    # Prosedur untuk melihat game yang dimiliki 
    # I.S dataKepemilikan, dataGame, user terdefinisi 
    # F.S Akan ditampilkan game yang dimiliki oleh user

    # KAMUS LOKAL
    # index, i, j : integer

    # ALGORITMA
    index = 0
    for i in range(1,Length(dataKepemilikan)):
        if dataKepemilikan[i][1] == user:
            for j in range(1,Length(dataGame)):
                if dataKepemilikan[i][0] == dataGame[j][0]:
                    index += 1
                    printRapihF09(dataGame, j, index)
    print()
    if index == 0:
        # User tidak memiliki game
        print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.\n")