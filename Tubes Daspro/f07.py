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

def list_game_toko(dataGame):
    skema = input("Skema sorting : ")
    if skema == 'tahun+':
        dataGame = sortingAscending(dataGame, 3)
        printRapihF07(dataGame)
    elif skema == 'tahun-':
        dataGame = sortingDescending(dataGame, 3)
        printRapihF07(dataGame)
    elif skema == 'harga+':
        dataGame = sortingAscending(dataGame, 4)
        printRapihF07(dataGame)
    elif skema == 'harga-':
        dataGame = sortingDescending(dataGame, 4)
        printRapihF07(dataGame)
    elif skema == '':
        dataGame = sortingAscending(dataGame,0)
    else:
        print("\nSkema sorting tidak valid!\n")
    return dataGame


