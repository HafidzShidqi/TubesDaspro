from fungsi import *

def search_my_game(userid, dataKepemilikan, dataGame):
    idGame = input("Masukkan ID Game: ")
    tahunRilis = input("Masukkan Tahun Rilis Game: ")

    arrayKepemilikan = []

    for i in range(1, Length(dataKepemilikan)):
        if dataKepemilikan[i][1] == userid:
            arrayKepemilikan += [dataGame[getIndexID(dataKepemilikan[i][0])]]
    
    index = 0

    print("\nDaftar game pada inventory yang memenuhi kriteria:")
    for i in range(Length(arrayKepemilikan)):
        if (arrayKepemilikan[i][0] == idGame or not idGame) and (arrayKepemilikan[i][3] == tahunRilis or not tahunRilis):
            index += 1
            printRapihF10(arrayKepemilikan, i, index)
    print()
    if index == 0:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria\n")

            

