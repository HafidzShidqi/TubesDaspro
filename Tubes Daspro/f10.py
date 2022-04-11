from konversiCSVToArray import *
from fungsi import *

def search_my_game (Inventory):
    # input
    inputid = input("Masukkan ID game: ")
    input_releaseyear = input("Masukkan tahun rilis game: ")
    
    if inputid != '':   # jika id game tidak kosong
        for i in range (Length(dataInventory)):
            if inputid == dataInventory[i][0]:
                printRapih(dataInventory[i])
    else:   # jika id game kosong (output seluruh game pada tahun rilis yang sama)
        for i in range (Length(dataInventory)):
            if input_releaseyear == dataInventory[i][3]:
                printRapih(dataInventory[i])