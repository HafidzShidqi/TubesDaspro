def GameArrayToCSV(lines):

    stringKosong = ''

    for line in lines:
        i = 0
        for str in line:
            if i < 5:
                stringKosong += str + ';'
                i += 1
            else:
                stringKosong += str
        stringKosong += '\n'

    return stringKosong

def UserArrayToCSV(lines):

    stringKosong = ''

    for line in lines:
        i = 0
        for str in line:
            if i < 5:
                stringKosong += str + ';'
                i += 1
            else:
                stringKosong += str
        stringKosong += '\n'

    return stringKosong


def RiwayatArrayToCSV(lines):

    stringKosong = ''

    for line in lines:
        i = 0
        for str in line:
            if i < 5:
                stringKosong += str + ';'
                i += 1
            else:
                stringKosong += str
        stringKosong += '\n'

    return stringKosong

# import os

# path = os.getcwd()
# os.chdir(path)

# newFolder = input("Masukkan nama folder penyimpanan: ")
# os.makedirs(newFolder)

# f = open(f'{newFolder}/game.csv', 'w')
# f.write('id;nama;kategori;tahun_rilis;harga;stok\nGAME001;BNMO - Play Along With Crypto;Adventure;2022;100000;1\nGAME002;Dasar Pemrograman;Coding;2022;0;10\nGAME003;Python Gemink;Coding;1991;69000;999')
# f.close()

# f = open(f'{newFolder}/user.csv', 'w')
# f.write('id;nama;kategori;tahun_rilis;harga;stok\nGAME001;BNMO - Play Along With Crypto;Adventure;2022;100000;1\nGAME002;Dasar Pemrograman;Coding;2022;0;10\nGAME003;Python Gemink;Coding;1991;69000;999')
# f.close()
