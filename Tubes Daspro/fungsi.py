def append(array1, array2):
    # function append (array1 : array or string , array2 : array or string) -> array
    # fungsi untuk menggabungkan array1 dan array2
    
    # KAMUS LOKAL
    # -

    # ALGORITMA UTAMA
    return array1 + array2

def isNum(string):
    # function isNum (string : integer or string) -> boolean
    # fungsi untuk check apakah 'string' berupa angka

    # KAMUS LOKAL
    # -

    # ALGORITMA UTAMA
    for char in string:
        if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90):
            return False
    return True

def Length(array):
    # function Length (array : array or string) -> integer
    # fungsi untuk menghitung panjang suatu array atau string

    # KAMUS LOKAL
    # length : integer
    # i : integer

    # ALGORITMA UTAMA
    length = 0
    for i in array:
        length += 1
    return length

def HighestLength(array, kolom):
    # function HighestLength (array : matrix , kolom : integer) -> integer
    # fungsi untuk menghitung panjang terbesar dari sebuah data pada matrix pada kolom ke-'kolom'

    # KAMUS LOKAL
    # highest : integer
    # i : integer

    # ALGORITMA UTAMA
    highest = 0
    for i in range(1, Length(array)):
        if Length(array[i][kolom]) > highest:
            highest = Length(array[i][kolom])
    return highest

def HighestLengthF10(array, kolom):
    # function HighestLength (array : matrix , kolom : integer) -> integer
    # sama dengan HighestLength akan tetapi fungsi ini khusus untuk f10.py

    # KAMUS LOKAL
    # highest : integer
    # i : integer

    # ALGORITMA UTAMA
    highest = 0
    for i in range(Length(array)):  # perbedaannya terletak pada range loopingnya
        if Length(array[i][kolom]) > highest:
            highest = Length(array[i][kolom])
    return highest

def getIndexID(id):
    # function getIndexID (id : string) -> integer
    # fungsi yang mengubah id game atau id user menjadi angka berupa integer
    # contoh getIndexID('GAME004') -> 4   ; getIndexID('USER010') -> 10

    # KAMUS LOKAL
    # -

    # ALGORITMA UTAMA
    return int(id[4])*100 + int(id[5])*10 + int(id[6])


def printRapihF07(array):
    # procudere printRapihF07 (input array : matrix) 
    # prosedur yang menampilkan output pada layar yang diminta seperti spesifikasi pada f07.py

    # KAMUS LOKAL
    # i : integer

    # ALGORITMA UTAMA
    for i in range(1,Length(array)):
        print(f"{i}. {array[i][0]}  | {array[i][1] + ' '*(HighestLength(array, 1) - Length(array[i][1])) } | {array[i][2] + ' '*(HighestLength(array, 2) - Length(array[i][2])) } | {array[i][3] + ' '*(HighestLength(array, 3) - Length(array[i][3])) } | {array[i][4] + ' '*(HighestLength(array, 4) - Length(array[i][4])) } | {array[i][5] + ' '*(HighestLength(array, 5) - Length(array[i][5])) }")

def printRapihF09(array, i, j):
    # procudere printRapihF09 (input array : matrix, input i : integer, input j : integer) 
    # prosedur yang menampilkan output pada layar yang diminta seperti spesifikasi pada f09.py

    # KAMUS LOKAL
    # -

    # ALGORITMA UTAMA
    print(f"{j}. {array[i][0]}  | {array[i][1] + ' '*(HighestLength(array, 1) - Length(array[i][1])) } | {array[i][2] + ' '*(HighestLength(array, 2) - Length(array[i][2])) } | {array[i][3] + ' '*(HighestLength(array, 3) - Length(array[i][3])) } | {array[i][4] + ' '*(HighestLength(array, 4) - Length(array[i][4])) }")

def printRapihF10(array, i, j):
    # procudere printRapihF09 (input array : matrix, input i : integer, input j : integer) 
    # prosedur yang menampilkan output pada layar yang diminta seperti spesifikasi pada f10.py

    # KAMUS LOKAL
    # -

    # ALGORITMA UTAMA
    print(f"{j}. {array[i][0]}  | {array[i][1] + ' '*(HighestLengthF10(array, 1) - Length(array[i][1])) } | {array[i][4] + ' '*(HighestLengthF10(array, 4) - Length(array[i][4])) } | {array[i][2] + ' '*(HighestLengthF10(array, 2) - Length(array[i][2])) } | {array[i][3] + ' '*(HighestLengthF10(array, 3) - Length(array[i][3]))}")

def printRapihF11(array, i, j):
    # procudere printRapihF09 (input array : matrix, input i : integer, input j : integer) 
    # prosedur yang menampilkan output pada layar yang diminta seperti spesifikasi pada f11.py

    # KAMUS LOKAL
    # -

    # ALGORITMA UTAMA
    print(f"{j}. {array[i][0]}  | {array[i][1] + ' '*(HighestLengthF10(array, 1) - Length(array[i][1])) } | {array[i][4] + ' '*(HighestLengthF10(array, 4) - Length(array[i][4])) } | {array[i][2] + ' '*(HighestLengthF10(array, 2) - Length(array[i][2])) } | {array[i][3] + ' '*(HighestLengthF10(array, 3) - Length(array[i][3])) } | {array[i][-1] + ' '*(HighestLengthF10(array, -1) - Length(array[i][-1])) }")

def printRapihF13(array, i, j):
    # procudere printRapihF09 (input array : matrix, input i : integer, input j : integer) 
    # prosedur yang menampilkan output pada layar yang diminta seperti spesifikasi pada f13.py

    # KAMUS LOKAL
    # -

    # ALGORITMA UTAMA
    print(f"{j}. {array[i][0]}  | {array[i][1] + ' '*(HighestLength(array, 1) - Length(array[i][1])) } | {array[i][2] + ' '*(HighestLength(array, 2) - Length(array[i][2])) } | {array[i][-1] + ' '*(HighestLength(array, -1) - Length(array[i][-1])) } |")