# import module os
import os

def createFolder(folderName):
    path = os.getcwd()
    os.chdir(path)
    os.makedirs(folderName)


def checkIsFolderValid(folderName):
    path = os.getcwd()
    folder = os.path.join(path, folderName)

    if not os.path.exists(folder):
        return False
    else:
        return True

def save(dataGame, dataUser):

    newFolder = input("Masukkan nama folder penyimpanan: ")

    if checkIsFolderValid(newFolder) == False:
        createFolder(newFolder)

    f = open(f'{newFolder}/game.csv', 'w')
    f.write(dataGame)
    f.close()

    f = open(f'{newFolder}/user.csv', 'w')
    f.write(dataUser)
    f.close()

    print("\nSaving...")
    print("Data telah disimpan pada folder", newFolder)


