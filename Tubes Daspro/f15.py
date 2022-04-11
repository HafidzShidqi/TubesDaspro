import argparse, os


def openFolder(folderName):

    # procedure openFolder (input folderName : str, output bisaLogin :  boolean, 
    #                       output path : boolean, output folderPath : boolean)
    # procedure untuk membuka dan check apakah folder dengan nama "folderName" valid atau tidak

    # KAMUS LOKAL
    # bisaLogin : boolean
    # path : str
    # folderPath : boolean


    # ALGORITMA 
    global bisaLogin
    # Deklarasi Variabel
    bisaLogin = False
    path = os.getcwd()  # Menghasilkan directory 
    folderPath = os.path.join(path, folderName) # Menghasilkan directory + folderName

    # Melakukan pengecheckan terhadap folderName
    if folderName == '':
        print("""Tidak ada nama folder yang diberikan!
        Usage: python program_binomo.py <nama_folder>
        """)
        bisaLogin = False
    elif not os.path.exists(folderPath):    # Jika folderName tidak ada pada folderPath
        print(f'Folder "{folderName}" tidak ditemukan.\n')
        bisaLogin = False
    elif os.path.exists(folderPath):        # Jika folderName ada dan sama dengan folderPath
        print("Loading...\n")
        print('Selamat datang di antarmuka "Binomo"\n')
        bisaLogin = True

def load():

    # function load (parser : module argparse) -> boolean
    # fungsi yang menerima string 'namaFolder' pada command line dan mereturn True jika 'namaFolder' ada

    # KAMUS LOKAL
    # parser, args : module argparse

    # ALGORITMA
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?', type=openFolder)
    args = parser.parse_args()
    return bisaLogin

    