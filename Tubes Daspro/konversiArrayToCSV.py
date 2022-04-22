def GameArrayToCSV(lines):
    # function GameArrayToCSV (lines : matrix) -> string
    # fungsi yang menerima matrix lalu mengubahnya menjadi string sesuai format untuk file csv

    # KAMUS LOKAL
    # stringKosong, line : string
    # i : integer

    # ALGORITMA UTAMA
    stringKosong = ''

    for line in lines:
        i = 0
        for str in line:
            if i < 5:   # jika kolom pada matrix lines < 5, maka akan memisahkan tiap data dengan ;
                stringKosong += str + ';'
                i += 1
            else:    
                stringKosong += str
        stringKosong += '\n'    # menambahkan data selanjutnya pada baris baru

    return stringKosong

def UserArrayToCSV(lines):
    # function UserArrayToCSV (lines : matrix) -> string
    # fungsi yang menerima matrix lalu mengubahnya menjadi string sesuai format untuk file csv

    # KAMUS LOKAL
    # stringKosong, line : string
    # i : integer

    # ALGORITMA UTAMA
    stringKosong = ''

    for line in lines:
        i = 0
        for str in line:
            if i < 5:   # jika kolom pada matrix lines < 5, maka akan memisahkan tiap data dengan ;
                stringKosong += str + ';'
                i += 1
            else:
                stringKosong += str
        stringKosong += '\n'    # menambahkan data selanjutnya pada baris baru

    return stringKosong

def RiwayatArrayToCSV(lines):
    # function RiwayatArrayToCSV (lines : matrix) -> string
    # fungsi yang menerima matrix lalu mengubahnya menjadi string sesuai format untuk file csv

    # KAMUS LOKAL
    # stringKosong, line : string
    # i : integer

    # ALGORITMA UTAMA
    stringKosong = ''

    for line in lines:
        i = 0
        for str in line:
            if i < 4:   # jika kolom pada matrix lines < 4, maka akan memisahkan tiap data dengan ;
                stringKosong += str + ';'
                i += 1
            else:
                stringKosong += str
        stringKosong += '\n'    # menambahkan data selanjutnya pada baris baru

    return stringKosong

def KepemilikanArrayToCSV(lines):
    # function KepemilikanArrayToCSV (lines : matrix) -> string
    # fungsi yang menerima matrix lalu mengubahnya menjadi string sesuai format untuk file csv

    # KAMUS LOKAL
    # stringKosong, line : string
    # i : integer

    # ALGORITMA UTAMA
    stringKosong = ''

    for line in lines:
        i = 0
        for str in line:
            if i < 1:   # jika kolom pada matrix lines < 1, maka akan memisahkan tiap data dengan ;
                stringKosong += str + ';'
                i += 1
            else:
                stringKosong += str
        stringKosong += '\n'    # menambahkan data selanjutnya pada baris baru

    return stringKosong
