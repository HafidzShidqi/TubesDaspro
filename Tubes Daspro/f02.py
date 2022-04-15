from konversiCSVToArray import *
from fungsi import *

def isUsernameValid(username):
    nonValid = 0
    for i in username:
        if ( (ord(i) == 45) or (47 < ord(i) < 58) or (64 < ord(i) < 91) or (ord(i) == 95) or (96 < ord(i) < 123)):
            continue
        else:
            nonValid += 1
    
    if nonValid == 0:
        return True
    else:
        return False

def register(dataUser):
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")
        
    terpakai = False    

    for i in range(1,Length(dataUser)):
        if str(dataUser[i][1]) == str(username):
            terpakai = True

    if isUsernameValid(username) == False:
        print('Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9\n')
    elif terpakai == False:
        id = str(Length(dataUser))
        for i in range(3-Length(id)): 
            id = append('0', id)    
        id = append('USER', id) 
        dataUser = append(dataUser, [[id,username, nama, password, "User", "0"]])
        print(f'\nUsername {username} telah berhasil register ke dalam "Binomo"\n')
    else:
        print(f'\nUsername {username} sudah terpakai, silakan menggunakan username lain\n')
    
    return dataUser

