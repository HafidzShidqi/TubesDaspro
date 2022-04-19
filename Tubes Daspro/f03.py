from fungsi import *

def login(dataUser):
    global userid
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    
    j = 0   #inisialisasi
    valid = False       #inisialisasi
    for i in range(1,Length(dataUser)):
        if dataUser[i][1] == username and dataUser[i][3] == password:
            valid = True
            j = i
    
    
    if valid == False:     #jika username dan password tidak sesuai   
        print("\nPassword atau username salah atau tidak ditemukan\n")
        return login(dataUser)      #memanggil fungsi login lagi
    else: #jika username dan password sesuai
        print(f'\nHalo {dataUser[j][2]}! Selamat datang di "Binomo".\n')    #dataUser[j][2] untuk menampilkan nama user
        userid = dataUser[j][0]     
        return dataUser[j][4]


