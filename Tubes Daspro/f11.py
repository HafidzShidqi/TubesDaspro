from konversiCSVToArray import *
from fungsi import *

def search_game_at_store ():
    gameid_search = input("Masukkan ID game: ")
    namagame_search = input("Masukkan nama game: ")
    harga_search = input("Masukkan harga game: ")
    kategori_search = input("Masukkan kategori game: ")
    trilis_search = input("Masukkan tahun rilis: ")

    if gameid_search != '':   
        for i in range (Length(dataGame)):
            if gameid_search == dataGame[i][0]:
                printRapih(dataGame[i])
    elif namagame_search != '':   
        for i in range (Length(dataGame)):
            if namagame_search == dataGame[i][1]:
                printRapih(dataGame[i])
    elif harga_search != '':  
        for i in range (Length(dataGame)):
            if harga_search == dataGame[i][4]:
                printRapih(dataGame[i])
    elif kategori_search != '':
        for i in range (Length(dataGame)):
            if kategori_search == dataGame[i][2]:
                printRapih(dataGame[i])
    elif trilis_search != '':
        for i in range (Length(dataGame[i])):
            if trilis_search == dataGame[i][3]:
                printRapih(dataGame[i])
