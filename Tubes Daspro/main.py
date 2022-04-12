import f15, konversiCSVToArray
import argparse, os


# f15.load() akan mereturn bisaLogin yang akan bernilai True jika nama folder valid dan program akan berjalan
if f15.bisaLogin == True:
    import f02, f03, f04, f05, f06, f07, f14, f16, f17, fungsi, konversiArrayToCSV
    # Deklarasi variabel sebagai tanda 
    checkExit = False
    isLogin = False
    # Mengubah CSV ke bentuk array dan disimpan dalam memori
    dataGame = konversiCSVToArray.GameCSVToArray()
    dataUser = konversiCSVToArray.UserCSVToArray()

    # Melakukan looping selama belum menjalankan perintah exit
    while checkExit == False:

        # Melakukan looping selama belum login
        while isLogin == False:
            # Akan meminta input, dan hanya berjalan jika input perintah == login
            perintah = input(">>>")
            if perintah == "login":
                role = f03.login()  # f03.login() akan mereturn value "Admin" atau "User"
                isLogin = True      # bernilai True sehingga akan keluar dari looping isLogin
            else:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”\n')
        
        # Setelah berhasil login, maka akan masuk ke dalam looping yang meminta perintah dari pengguna

        # jika rolenya Admin, maka check perintah yang bisa dilakukan oleh admin dan menjalankan perintahnya
        if role == 'Admin':
            perintah = input(">>>")
            if perintah == "login":
                print("Anda sudah login.\n")
            elif perintah == "help":
                f14.help(role)
            elif perintah == "register":
                dataUser = f02.register()       # menjalankan register dan datanya disimpan dalam memori
            elif perintah == "tambah_game":
                dataGame = f04.tambah_game()    # menjalankan tambah_game dan datanya disimpan dalam memori
            elif perintah == "ubah_game":
                dataGame = f05.ubah_game(dataGame) # menjalankan ubah_game dan datanya disimpan dalam memori
            elif perintah == "ubah_stok":
                dataGame = f06.ubah_stok(dataGame) # menjalankan ubah_stok dan datanya disimpan dalam memori
            elif perintah == "list_game_toko":
                dataGame = f07.list_game_toko(dataGame) # menjalankan list_game_toko
            elif perintah == "exit":
                f17.exit(dataGame, dataUser)    # menjalankan exit 
                checkExit = True                # dan akan keluar dari program
            else:   # jika perintah selain di atas, maka perintah tersebut hanya bisa diakses oleh 'User'
                print("Perintah hanya bisa dilakukan oleh User")  
        elif role == 'User':
            perintah = input(">>>")
            if perintah == "login":
                print("Anda sudah login.\n")
            elif perintah == "help":
                f14.help(role)
            elif perintah == "list_game_toko":
                dataGame = f07.list_game_toko(dataGame)
            elif perintah == "exit":
                f17.exit(dataGame, dataUser)
                checkExit = True
            else:
                print("Perintah hanya bisa dilakukan oleh Admin")
        
                



    


