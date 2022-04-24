from f16 import *
from konversiArrayToCSV import *

def exit(dataGame, dataUser, dataKepemilikan, dataRiwayat):
    
    # procedure exit (input dataGame : array, input dataUser : array, input dataKepemilikan : array, input dataRiwayat : array)
    # {I.S. Menerima Menerima matrix dataGame, dataUser, dataKepemilikan, dan dataRiwayat dan validasi apakah ingin menyimpan file atau tidak } 
    # {F.S. Jika user ingin menyimpan file, makan jalankan procedure save dan keluar dari program }
    # {F.S. Jika user tidak ingin menyimpan file, maka akan keluar dari pr 

    # KAMUS LOKAL
    # askExit : string

    # ALGORITMA UTAMA
    # Looping untuk validasi jawaban ingin menyimpan file atau tidak
    while True:
        askExit = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if askExit == "Y" or askExit == "y":
            save(GameArrayToCSV(dataGame), UserArrayToCSV(dataUser), KepemilikanArrayToCSV(dataKepemilikan), RiwayatArrayToCSV(dataRiwayat))
            break
        elif askExit == 'N' or askExit == 'n':
            break
        else:
            print('Hasil input tidak valid!\n')