from fungsi import *

def riwayat(user, dataRiwayat):
    index = 0
    for i in range(1, Length(dataRiwayat)):
        if dataRiwayat[i][3] == user:
            index += 1
            printRapihF13(dataRiwayat, i, index)
    print()
    if index == 0:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.\n")

