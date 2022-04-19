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
    elif isNum(tahun_rilis) == False or isNum(harga) == False or isNum(stok_awal) == False:
        print("\nTahun Rilis atau Harga atau Stok Awal harus berupa integer!\n")
        tambah_game()
    elif int(tahun_rilis) < 0 or int(harga) < 0 or int(stok_awal) < 0:
        print("\nTahun Rilis atau Harga atau Stok Awal tidak boleh bernilai negatif!\n")
        tambah_game()
    else:
        print(f"\nSelamat! Berhasil menambahkan game {nama}\n")
        id = str(Length(dataGame))
        for i in range(3-Length(id)):
            id = append('0', id)
        id = append('GAME', id)
        dataGame = append(dataGame, [[id, nama, kategori, tahun_rilis, harga, stok_awal]])
    
    return dataGame

