from fungsi import *

def search_my_game(userid, dataKepemilikan, dataGame):
    # Procedure search_my_game(input userid : string, dataKepemilikan : array, dataGame : array)
    # procedure untuk mencari game yang telah dimiliki berdasarkan input id game atau/dan tahun rilis
    # I.S pengguna memasukan id atau/dan tahun dari game yang ingin dicari
    # F.S pada layar muncul game yang dicari
    
    # KAMUS
    # idGame, dataKepemilikan[i][1], dataKepemilikan[i][0]  : string
	# tahunRilis, index :  integer
	# arrayKepemilikan : array
    
    # ALGORITMA

    # input
    idGame = input("Masukkan ID Game: ")
    tahunRilis = input("Masukkan Tahun Rilis Game: ")
    
    # deklarasi array kosong
    arrayKepemilikan = []

    # menggunakan loop untuk menyamakan id user agar mendapatkan data
    for i in range(1, Length(dataKepemilikan)):
        if dataKepemilikan[i][1] == userid:
            arrayKepemilikan += [dataGame[getIndexID(dataKepemilikan[i][0])]]
    
    # deklarasi index
    index = 0
    
    # output pencarian
    print("\nDaftar game pada inventory yang memenuhi kriteria:")
    for i in range(Length(arrayKepemilikan)):
        if (arrayKepemilikan[i][0] == idGame or not idGame) and (arrayKepemilikan[i][3] == tahunRilis or not tahunRilis):
            index += 1
            printRapihF10(arrayKepemilikan, i, index)   # jika hasil pencarian ada
    print()
    if index == 0:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria\n")  # jika hasil pencarian tidak ada

            

