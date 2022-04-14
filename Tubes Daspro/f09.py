from fungsi import *

def list_game(user, dataKepemilikan, dataGame):
    index = 0
    for i in range(1,Length(dataKepemilikan)):
        if dataKepemilikan[i][1] == user:
            for j in range(1,Length(dataGame)):
                if dataKepemilikan[i][0] == dataGame[j][0]:
                    index += 1
                    printRapihF09(dataGame, j, index)
    if index == 0:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")