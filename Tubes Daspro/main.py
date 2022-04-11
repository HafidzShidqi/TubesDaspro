import f02, f03, f04, f05, f06, f07, f14, f15, f16, f17, fungsi, konversiCSVToArray, konversiArrayToCSV
import argparse, os


if f15.load() == True:
    checkExit = False
    isLogin = False
    dataGame = konversiCSVToArray.GameCSVToArray()
    dataUser = konversiCSVToArray.UserCSVToArray()
    while checkExit == False:
        while isLogin == False:
            perintah = input()
            if perintah == "login":
                role = f03.login()
                isLogin = True
            else:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”\n')
        if role == 'Admin':
            perintah = input()
            if perintah == "login":
                print("Anda sudah login.\n")
            elif perintah == "help":
                help(role)
            elif perintah == "register":
                dataUser = f02.register()
            elif perintah == "tambah_game":
                dataGame = f04.tambah_game()
            elif perintah == "ubah_game":
                dataGame = f05.ubah_game(dataGame)
            elif perintah == "ubah_stock":
                dataGame = f06.ubah_stok(dataGame)
            elif perintah == "list_game_toko":
                dataGame = f07.list_game_toko(dataGame)
            elif perintah == "exit":
                f17.exit(dataGame, dataUser)
                checkExit = True
            else:
                print("Perintah hanya bisa dilakukan oleh User")
                
        elif role == 'User':
            perintah = input()
            if perintah == "login":
                print("Anda sudah login.\n")
            elif perintah == "help":
                help(role)
            elif perintah == "list_game_toko":
                dataGame = f07.list_game_toko(dataGame)
            elif perintah == "exit":
                f17.exit(dataGame, dataUser)
                checkExit = True
            else:
                print("Perintah hanya bisa dilakukan oleh Admin")
        
                



    


