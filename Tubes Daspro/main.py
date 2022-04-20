import f15, konversiCSVToArray
from fungsi import *
import argparse, os


# f15.load() akan mereturn bisaLogin yang akan bernilai True jika nama folder valid dan program akan berjalan
if f15.bisaLogin == True:
    import f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f16, f17, konversiArrayToCSV
    # Deklarasi variabel sebagai tanda 
    checkExit = False
    isLogin = False
    # Mengubah CSV ke bentuk array dan disimpan dalam memori
    dataGame = konversiCSVToArray.GameCSVToArray()
    dataUser = konversiCSVToArray.UserCSVToArray()
    dataKepemilikan = konversiCSVToArray.kepemilikanCSVToArray()
    dataRiwayat = konversiCSVToArray.riwayatCSVToArray()
    # Melakukan looping selama belum menjalankan perintah exit
    while checkExit == False:

        # Melakukan looping selama belum login
        while isLogin == False:
            # Akan meminta input, dan hanya berjalan jika input perintah == login
            perintah = input(">>> ")
            if perintah == "login":
                role = f03.login(dataUser)  # f03.login() akan mereturn value "Admin" atau "User"
                isLogin = True      # bernilai True sehingga akan keluar dari looping isLogin
            else:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”\n')
        
        # Setelah berhasil login, maka akan masuk ke dalam looping yang meminta perintah dari pengguna

        # jika rolenya Admin, maka check perintah yang bisa dilakukan oleh admin dan menjalankan perintahnya
        if role == 'Admin':
            perintah = input(">>> ")
            if perintah == "login":
                print("Anda sudah login.\n")
            elif perintah == "register":
                dataUser = f02.register(dataUser)
            elif perintah == "tambah_game":
                dataGame = f04.tambah_game(dataGame)    
            elif perintah == "ubah_game":
                dataGame = f05.ubah_game(dataGame) 
            elif perintah == "ubah_stok":
                dataGame = f06.ubah_stok(dataGame) 
            elif perintah == "list_game_toko":
                dataGame = f07.list_game_toko(dataGame) 
            elif perintah == "search_game_at_store":
                f11.search_game_at_store(dataGame)
            elif perintah == "topup":
                dataUser = f12.topup(dataUser)
            elif perintah == "help":
                f14.help(role)
            elif perintah == "exit":
                f17.exit(dataGame, dataUser, dataKepemilikan, dataRiwayat)    
                checkExit = True                
            elif perintah == "buy_game" or perintah == "list_game" or perintah == "search_my_game" or perintah == "riwayat":
                print("Perintah hanya bisa dilakukan oleh User\n")  
            else:
                print("Tidak mengenali perintah!\n")
        elif role == 'User':
            perintah = input(">>> ")
            if perintah == "login":
                print("Anda sudah login.\n")
            elif perintah == "list_game_toko":
                dataGame = f07.list_game_toko(dataGame) 
            elif perintah == "buy_game":
                print(f'Saldo sekarang : {dataUser[getIndexID(f03.userid)][-1]}')
                dataGame, dataUser, dataKepemilikan, dataRiwayat = f08.buy_game(f03.userid, dataGame, dataUser, dataKepemilikan, dataRiwayat)
            elif perintah == "list_game":
                f09.list_game(f03.userid, dataKepemilikan, dataGame)
            elif perintah == "search_my_game":
                f10.search_my_game(f03.userid, dataKepemilikan, dataGame)
            elif perintah == "search_game_at_store":
                f11.search_game_at_store(dataGame)
            elif perintah == "riwayat":
                f13.riwayat(f03.userid, dataRiwayat)
            elif perintah == "help":
                f14.help(role)
            elif perintah == "exit":
                f17.exit(dataGame, dataUser, dataKepemilikan, dataRiwayat) 
                checkExit = True
            elif perintah == "register" or perintah == "tambah_game" or perintah == "ubah_game" or perintah == "ubah_stok" or perintah == "topup":
                print("Perintah hanya bisa dilakukan oleh Admin\n")
            else:
                print("Tidak mengenali perintah!\n")
        
                



    


