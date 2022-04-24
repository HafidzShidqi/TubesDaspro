from fungsi import *

def riwayat(user, dataRiwayat):
    # Procedure riwayat(input user: string, dataRiwayat: array)
	# Prosedur untuk menampilkan riwayat pembelian game dari user
	# I.S array terdefinisi
	# F.S data akan ditampilkan pada layar 
	
    # KAMUS
	# index, i : integer
	# dataRiwayat[i][3], user : string
	
    # ALGORITMA
    # deklarasi index
    index = 0
    
    # loop untuk menyesuaikan hasil pencarian (riwayat)
    for i in range(1, Length(dataRiwayat)):
        if dataRiwayat[i][3] == user:
            index += 1
            printRapihF13(dataRiwayat, i, index)    # output hasil pencarian jika ada
    print()
    if index == 0:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game untuk membeli.\n")  # output hasil pencarian jika tidak ada

