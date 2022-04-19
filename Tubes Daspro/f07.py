from konversiCSVToArray import *
from fungsi import *

def sortingDescending(array, atribut):
    for i in range(1, Length(array)-1):
        for j in range(1,Length(array)-1):
            if int(array[j][atribut]) < int(array[j+1][atribut]):
                array[j], array[j+1] = array[j+1], array[j]
    return array

def sortingAscending(array, atribut):
    for i in range(1, Length(array)-1):
        for j in range(1, Length(array)-1):
            if int(array[j][atribut]) > int(array[j+1][atribut]):
                array[j], array[j+1] = array[j+1], array[j]
    return array

def sortingAscendingByGameId(array):
    for i in range(1, Length(array)-1):
        for j in range(1, Length(array)-1):
            if getIndexID(array[j][0]) > getIndexID(array[j+1][0]):
                array[j], array[j+1] = array[j+1], array[j]
    return array


def list_game_toko(dataGame):
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

