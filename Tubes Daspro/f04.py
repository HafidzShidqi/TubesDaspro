from konversiCSVToArray import *
from fungsi import *

dataGame = GameCSVToArray()

def tambah_game():
    global dataGame
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    stok_awal = input("Masukkan stok awal: ")

    if nama == '' or kategori == '' or tahun_rilis == '' or harga == '' or stok_awal == '':
        print("\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.\n")
        tambah_game()
    else:
        print(f"\nSelamat! Berhasil menambahkan game {nama}\n")
        id = str(Length(dataGame))
        for i in range(3-Length(id)):
            id = append('0', id)
        id = append('GAME', id)
        dataGame = append(dataGame, [[id, nama, kategori, tahun_rilis, harga, stok_awal]])
    
    return dataGame

