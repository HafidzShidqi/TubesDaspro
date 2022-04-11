from f16 import *
from konversiArrayToCSV import *
from konversiCSVToArray import *

def exit(dataGame, dataUser):
    while True:
        askExit = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if askExit == "Y" or askExit == "y":
            save(GameArrayToCSV(dataGame), UserArrayToCSV(dataUser))
            break
        elif askExit == 'N' or askExit == 'n':
            break