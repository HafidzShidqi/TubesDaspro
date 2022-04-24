from fungsi import *

def sortingDescending(array, atribut):
    # Procedure sortingDescending(input/output array : array, input atribut) 
    # Prosedur untuk mengurutkan berdasarkan atribut dan descending 
    # I.S array dan atribut terdefinisi
    # F.S array terurut sesuai atribut dan descending
    
    # KAMUS LOKAL
    # i, j : integer

    # ALGORITMA
    for i in range(1, Length(array)-1):
        for j in range(1,Length(array)-1):
            if int(array[j][atribut]) < int(array[j+1][atribut]):
                array[j], array[j+1] = array[j+1], array[j]
    return array

def sortingAscending(array, atribut):
    # procedure sortingAscending(input/output array : array, input atribut) 
    # Prosedur untuk mengurutkan berdasarkan atribut secara ascending 
    # I.S array dan atribut terdefinisi 
    # F.S array terurut sesuai atribut secara ascending} 

    # KAMUS LOKAL
    # i, j : integer

    # ALGORITMA
    for i in range(1, Length(array)-1):
        for j in range(1, Length(array)-1):
            if int(array[j][atribut]) > int(array[j+1][atribut]):
                array[j], array[j+1] = array[j+1], array[j]
    return array

def sortingAscendingByGameId(array):
    # Procedure sortingAscendingByGameId(input/output array : array) 
    # Prosedur untuk mengurutkan berdasarkan GameId secara ascending 
    # I.S array terdefinisi 
    # F.S data akan terurut berdasarkan GameId secara ascending

    # KAMUS LOKAL
    # i, j : integer

    # ALGORITMA
    for i in range(1, Length(array)-1):
        for j in range(1, Length(array)-1):
            if getIndexID(array[j][0]) > getIndexID(array[j+1][0]):
                array[j], array[j+1] = array[j+1], array[j]
    return array


def list_game_toko(dataGame):
    # procedure list_game_toko(input/output dataGame : array) 
    # Fungsi untuk melakukan list pada dataGame berdasarkan beberapa skema yakni, tahun, harga, dan GameId 
    # I.S dataGame terdefinisi dan ada 
    # F.S ditampilkan dataGame yand sudah terurut sesuai skema yang diinginkan ke layar dan lalu 
    #     dataGame diurut secara ID menaik secara default 

    # KAMUS LOKAL
    # skema : string

    # ALGORITMA
    skema = input("Skema sorting : ")
    if skema == 'tahun+':
        printRapihF07(sortingAscending(dataGame, 3))
        print()
    elif skema == 'tahun-':
        printRapihF07(sortingDescending(dataGame, 3))
        print()
    elif skema == 'harga+':
        printRapihF07(sortingAscending(dataGame, 4))
        print()
    elif skema == 'harga-':
        printRapihF07(sortingDescending(dataGame, 4))
        print()
    elif skema == '':
        printRapihF07(sortingAscendingByGameId(dataGame))
        print()
    else:
        print("\nSkema sorting tidak valid!\n")
    return sortingAscendingByGameId(dataGame)

