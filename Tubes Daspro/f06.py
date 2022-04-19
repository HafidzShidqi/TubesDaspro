from konversiCSVToArray import *
from fungsi import *

def ubah_stok(dataGame):
    id = input("Masukkan ID game: ")
    jumlah = int(input("Masukkan jumlah: "))
    foundID = False     #inisialisasi
    for i in range(Length(dataGame)):
        if dataGame[i][0] == id:    #cek id
            foundID = True          #jika id ditemukan di data game.csv
            stok = int(dataGame[i][-1]) #mengakses stok yang ada pada kolom terakhir di dataGame
            if stok + jumlah < 0:       
                print(f"Stok game {dataGame[i][1]} gagal dikurangi karena stok kurang. Stok sekarang: {dataGame[i][-1]} (< {jumlah * -1})\n")
            else:
                if jumlah < 0:
                    dataGame[i][-1] = str(stok + jumlah)
                    print(f"Stok game {dataGame[i][1]} berhasil dikurangi. Stok sekarang: {stok + jumlah}\n")
                else:
                    dataGame[i][-1] = str(stok + jumlah)
                    print(f"Stok game {dataGame[i][1]} berhasil ditambahkan. Stok sekarang: {stok + jumlah}\n")
    if foundID == False:    #jika id tidak ditemukan di data game.csv
        print("\nTidak ada game dengan ID tersebut!")
    return dataGame

