import argparse, os

def load():

    # function load (folderName : string) -> (if bisaLogin = True -> string ; else -> boolean)
    # fungsi yang menerima folderName dan mengecheck apakah folder tersebut ada
    # jika ada, maka akan mengembalikan folderName dan akan menjalankan program
    # jika tidak, maka akan mereturn False sehingga tidak bisa menjalankan program


    # KAMUS LOKAL
    # bisaLogin : boolean
    # parser, args : variabel module argparse
    # path, folderPath : string

    # ALGORITMA UTAMA
    global bisaLogin
    
    bisaLogin = False

    # Membuat parser
    parser = argparse.ArgumentParser()
    parser.add_argument("folderName", nargs ="?")
    args = parser.parse_args()

    # Jika pengguna menginput nama foldeer yang kosong, maka:
    if not args.folderName:
        print("""Tidak ada nama folder yang diberikan!
Usage: python main.py <nama_folder>""")
        bisaLogin = False
        return False
    else:   # Jika nama folder ada, maka:
        # Membuat directory dimana folderName yang diinput oleh pengguna disimpan dalam PC/Laptop
        path = os.getcwd()  
        folderPath = os.path.join(path, args.folderName)
        # Jika folderName tidak ada pada folderPath
        if not os.path.exists(folderPath):     
            print(f'Folder "{args.folderName}" tidak ditemukan.\n')
            bisaLogin = False                   
            return False
        elif os.path.exists(folderPath):        # Jika folderName ada dan sama dengan folderPath
            print("Loading...\n")
            print('Selamat datang di antarmuka "Binomo"\n')
            bisaLogin = True
            return args.folderName              # program utama akan dijalankan

