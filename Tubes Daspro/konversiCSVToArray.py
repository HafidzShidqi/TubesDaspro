from f15 import *

# deklarasi variabel, sekaligus menjalankan fungsi load() dari f15
folderName = load() 

# check apakah fungsi load() mereturn True atau False, jika tidak False maka akan menjalankan program
if folderName != False:
    def GameCSVToArray():
        # function GameCSVToArray() -> matrix of string
        # fungsi yang mengubah file game.csv menjadi matrix

        # KAMUS LOKAL
        # f : TextIOWrapper
        # lines, line, char : string
        # dataGame : matrix of string
        # n : integer
        # line_data : array of string

        # ALGORITMA UTAMA
        global dataGame

        # Membaca file game.csv pada folder "folderName"
        f = open(f"{folderName}/game.csv", "r")
        lines = f.readlines()
        f.close()

        dataGame = []

        # Melakukan looping untuk mengkonversi game.csv ke matrix 
        for line in lines:
            n = 0
            line_data = ['']
            for char in line:   
                if char == ';':    
                    line_data += ['']
                    n += 1
                elif char != '\n':
                    line_data[n] += char  

            dataGame += [line_data]

        return dataGame

    def UserCSVToArray():
        # function GameCSVToArray() -> matrix of string
        # fungsi yang mengubah file user.csv menjadi matrix

        # KAMUS LOKAL
        # f : TextIOWrapper
        # lines, line, char : string
        # dataUser : matrix of string
        # n : integer
        # line_data : array of string

        # ALGORITMA UTAMA
        global dataUser

        # Membaca file user.csv pada folder "folderName"
        f = open(f"{folderName}/user.csv", "r")
        lines = f.readlines()
        f.close()

        dataUser = []

        # Melakukan looping untuk mengkonversi user.csv ke matrix 
        for line in lines:
            n = 0
            line_data = ['']
            for char in line:
                if char == ';':
                    line_data += ['']
                    n += 1
                elif char != '\n':
                    line_data[n] += char

            dataUser += [line_data]

        return dataUser

    def riwayatCSVToArray():
        # function GameCSVToArray() -> matrix of string
        # fungsi yang mengubah file riwayat.csv menjadi matrix

        # KAMUS LOKAL
        # f : TextIOWrapper
        # lines, line, char : string
        # dataRiwayat : matrix of string
        # n : integer
        # line_data : array of string

        # ALGORITMA UTAMA
        global dataRiwayat

        # Membaca file riwayat.csv pada folder "folderName"
        f = open(f"{folderName}/riwayat.csv", "r")
        lines = f.readlines()
        f.close()

        dataRiwayat = []

        # Melakukan looping untuk mengkonversi riwayat.csv ke matrix 
        for line in lines:
            n = 0
            line_data = ['']
            for char in line:
                if char == ';':
                    line_data += ['']
                    n += 1
                elif char != '\n':
                    line_data[n] += char

            dataRiwayat += [line_data]

        return dataRiwayat

    def kepemilikanCSVToArray():
        # function GameCSVToArray() -> matrix of string
        # fungsi yang mengubah file game.csv menjadi matrix

        # KAMUS LOKAL
        # f : TextIOWrapper
        # lines, line, char : string
        # dataKepemilikan : matrix of string
        # n : integer
        # line_data : array of string

        # ALGORITMA UTAMA
        global dataKepemilikan

        # Membaca file kepemilikan.csv pada folder "folderName"
        f = open(f"{folderName}/kepemilikan.csv", "r")
        lines = f.readlines()
        f.close()

        dataKepemilikan = []

        # Melakukan looping untuk mengkonversi kepemilikan.csv ke matrix 
        for line in lines:
            n = 0
            line_data = ['']
            for char in line:
                if char == ';':
                    line_data += ['']
                    n += 1
                elif char != '\n':
                    line_data[n] += char

            dataKepemilikan += [line_data]

        return dataKepemilikan
