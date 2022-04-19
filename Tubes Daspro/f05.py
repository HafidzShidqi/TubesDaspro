from konversiCSVToArray import *
from fungsi import *

def ubah_game(dataGame):
    id = input("Masukkan ID game: ")
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    foundID = False     #inisialisasi
    for i in range(Length(dataGame)):
        if dataGame[i][0] == id:        #cek id
            foundID = True
            if nama != '':              #jika input "" maka datanya akan sama dengan data awal
                dataGame[i][1] = nama
            if kategori != '':
                dataGame[i][2] = kategori
            if tahun_rilis!= '':
                dataGame[i][3] = tahun_rilis
            if harga != '':
                dataGame[i][4] = harga

    if foundID == False: #jika id tidak ada di data
        print("\nTidak ada game dengan ID tersebut!\n")
    else: #jika id ada di data
        print("\nBerhasil mengubah game!\n")
    
    return dataGame




