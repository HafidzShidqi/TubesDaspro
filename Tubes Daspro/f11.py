from fungsi import *

def search_game_at_store(dataGame):
    # Procedure search_game_at_store(input dataGame: array)
    # Prosedur untuk menampilkan game yang dicari di toko sesuai input yang dimasukan 
    # I.S pengguna memasukan ID, nama, harga, kategori, atau/dan tahun rilis game
    # F.S Muncul game yang dicari
    # KAMUS
    # idGame, namaGame, kategoriGame,dataGame[i][0], dataGame[i][1], dataGame[i][2] : string
    # hargaGame, tahunRilis, dataGame[i][4], dataGame[i][3]:  integer
    
    # ALGORITMA
    # input
    idGame = input("Masukkan ID Game: ")
    namaGame = input("Masukkan Nama Game: ")
    hargaGame = input("Masukkan Harga Game: ")
    kategoriGame = input("Masukkan Kategori Game: ")
    tahunRilis = input("Masukkan Tahun Rilis Game: ")
    
    # deklarasi index dan variabel valid
    index = 0
    valid = False
    
    # loop untuk mencari elemen yang diinginkan
    for i in range(1,Length(dataGame)):
        if (dataGame[i][0] == idGame or not idGame) and (dataGame[i][1] == namaGame or not namaGame) and (dataGame[i][4] == hargaGame or not hargaGame) and (dataGame[i][2] == kategoriGame or not kategoriGame) and (dataGame[i][3] == tahunRilis or not tahunRilis):
            valid = True
            index += 1
            printRapihF11(dataGame, i, index)   # output pencarian
    print()
    
        # output jika hasil pencarian tidak ada
    if valid == False:
        print("\nTidak ada game dengan spesifikasi tersebut!\n")
    
