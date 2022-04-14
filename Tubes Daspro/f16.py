# import module os
import os

def createFolder(folderName):

    # procedure createFolder (input folderNmae : string,  output path : string)
    # prosedur yang membuat folder dengan nama folder = "folderName" berupa input dari pengguna
    # {I.S. Menerima input "folderName" berupa string,   F.S. Membuat folder dengan nama "folderName"}

    # KAMUS LOKAL
    # path, folderName : str

    #ALGORITMA
    path = os.getcwd()          # Menangkap directory dan nilainya disimpan dalam variabel path
    os.chdir(path)              # Mengganti directory menjadi path
    os.makedirs(folderName)     # Membuat folder "folderName" pada path


def checkIsFolderValid(folderName):

    # function checkIsFolderValid (folderName : string) -> boolean
    # mengecheck "folderName" pada directory 
    # jika "folderName" terdapat pada directory akan mereturn True dan sebaliknya

    # KAMUS LOKAL
    # path, folder : str

    # ALGORITMA
    path = os.getcwd()  # Menangkap directory
    folder = os.path.join(path, folderName) # Memiliki value : directory/"folderName"

    # Melakukan pengecheckan variabel folder
    if not os.path.exists(folder):
        return False
    else:
        return True


def save(dataGame, dataUser, dataKepemilikan, dataRiwayat):

    # procedure save (input/output dataGame : string,  input/ouput dataUser : string)
    # {I.S. Menerima input dataGame dan dataUser}
    # {F.S. Menyimpan dataGame pada game.csv, dataUser pada user.csv pada folder "newFolder" yang berupa input dari pengguna}

    # KAMUS LOKAL
    # newFolder : string

    # ALGORITMA
    newFolder = input("Masukkan nama folder penyimpanan: ")

    # check apakah folder "newFolder" sudah ada
    if checkIsFolderValid(newFolder) == False:
        createFolder(newFolder) # jika belum, maka buat folder dengan nama "newFolder"

    # Membuat file game.csv dengan isi dari dataGame pada folder "newFolder"
    f = open(f'{newFolder}/game.csv', 'w')
    f.write(dataGame)
    f.close()

    # Membuat file user.csv dengan isi dari dataGame pada folder "newFolder"
    f = open(f'{newFolder}/user.csv', 'w')
    f.write(dataUser)
    f.close()

    f = open(f'{newFolder}/kepemilikan.csv', 'w')
    f.write(dataKepemilikan)
    f.close()

    f = open(f'{newFolder}/riwayat.csv', 'w')
    f.write(dataRiwayat)
    f.close()

   

    print("\nSaving...")
    print("Data telah disimpan pada folder", newFolder)


