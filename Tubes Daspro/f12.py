from konversiCSVTArray import *
from fungsi import *

def topup():
        # input
        user_search = input("Masukan username: ")
        saldo_input = input("Masukan saldo: ")
        count = 0

        # pengecekan validasi saldo
        if saldo_input <= 0:
                print("Masukan tidak valid")
        else:
                for i in range (Length(dataUser)): 
                        if user_search == dataUser[i][1]:  # username ditemukan
                                datauser[i][5] == datauser[i][5] + saldo_input
                                print("Top up berhasil. saldo " + str(datauser[i][1] + "bertambah menjadi " + str(datauser[i][2])))
                        else:           #username tidak ditemukan
                                count = count + 1
                
                        if count == Length(array): # username tidak ditemukan
                                print("Username" + str(user_search) + " tidak ditemukan")