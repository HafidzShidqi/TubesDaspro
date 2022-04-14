from fungsi import *

def search_game_at_store(dataGame):
    idGame = input("Masukkan ID Game: ")
    namaGame = input("Masukkan Nama Game: ")
    hargaGame = input("Masukkan Harga Game: ")
    kategoriGame = input("Masukkan Kategori Game: ")
    tahunRilis = input("Masukkan Tahun Rilis Game: ")

    index = 0
    valid = False
    for i in range(1,Length(dataGame)):
        if (dataGame[i][0] == idGame or not idGame) and (dataGame[i][1] == namaGame or not namaGame) and (dataGame[i][4] == hargaGame or not hargaGame) and (dataGame[i][2] == kategoriGame or not kategoriGame) and (dataGame[i][3] == tahunRilis or not tahunRilis):
            valid = True
            index += 1
            printRapihF11(dataGame, i, index)
    
    if valid == False:
        print("Tidak ada game dengan spesifikasi tersebut!")
    
