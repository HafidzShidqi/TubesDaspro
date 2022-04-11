from fungsi import Length
from konversiCSVToArray import *

dataUser = UserCSVToArray()

def login():
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    
    j = 0
    valid = False
    for i in range(1,Length(dataUser)):
        if dataUser[i][1] == username and dataUser[i][3] == password:
            valid = True
            j = i
    
    if valid == False:
        print("Password atau username salah atau tidak ditemukan\n")
        return login()
    else:
        print(f'Halo {dataUser[j][2]}! Selamat datang di "Binomo".\n')
        return dataUser[j][4]


        

