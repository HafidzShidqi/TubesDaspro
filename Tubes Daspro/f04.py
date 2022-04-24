from fungsi import *

def tambah_game(dataGame):
    # Procedure tambah_game(input/output dataGame : array) 
    # prosedur untuk menambah game ke dalam array dataGame
    # {I.S dataGame adalah konversi array dari game.csv}
    # {F.S dataGame akan ditambah dengan game yang baru}

    # KAMUS LOKAL
    # nama, kategori, tahun_rilis, harga, strok_awal, id : string

    # AlGORITMA
    while True :
        nama = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok_awal = input("Masukkan stok awal: ")

        # Validasi input
        if nama == '' or kategori == '' or tahun_rilis == '' or harga == '' or stok_awal == '': 
            # Terdapat input kosong
            print("\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.\n")
        elif isNum(tahun_rilis) == False or isNum(harga) == False or isNum(stok_awal) == False:
            # Pada tahun_rilis, harga, atau stok_awal terdapat input bukan integer
            print("\nTahun Rilis atau Harga atau Stok Awal harus berupa integer!\n")
        elif int(tahun_rilis) < 0 or int(harga) < 0 or int(stok_awal) < 0:
            # Pada tahun_rilis, harga, atau stok_awal terdapat input bilangan negatf
            print("\nTahun Rilis atau Harga atau Stok Awal tidak boleh bernilai negatif!\n")
        else: 
            # Input sudah valid
            print(f"\nSelamat! Berhasil menambahkan game {nama}\n")

            # Mendapatkan id game baru
            id = str(Length(dataGame))
            for i in range(3-Length(id)):
                id = append('0', id)
            id = append('GAME', id)

            # Menambahkan ke dataGame
            dataGame = append(dataGame, [[id, nama, kategori, tahun_rilis, harga, stok_awal]])
            break

    return dataGame