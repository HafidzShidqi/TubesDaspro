def append(array1, array2):
    return array1 + array2

def isNum(string):
    for char in string:
        if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90):
            return False
    return True

def Length(array):
    length = 0
    for i in array:
        length += 1
    return length

def HighestLength(array, kolom):
    highest = 0
    for i in range(1, Length(array)):
        if Length(array[i][kolom]) > highest:
            highest = Length(array[i][kolom])
    return highest

def HighestLengthF10(array, kolom):
    highest = 0
    for i in range(Length(array)):
        if Length(array[i][kolom]) > highest:
            highest = Length(array[i][kolom])
    return highest

def getIndexID(id):
    return int(id[4])*100 + int(id[5])*10 + int(id[6])

def printRapihF07(array):
    for i in range(1,Length(array)):
        print(f"{i}. {array[i][0]}  | {array[i][1] + ' '*(HighestLength(array, 1) - Length(array[i][1])) } | {array[i][2] + ' '*(HighestLength(array, 2) - Length(array[i][2])) } | {array[i][3] + ' '*(HighestLength(array, 3) - Length(array[i][3])) } | {array[i][4] + ' '*(HighestLength(array, 4) - Length(array[i][4])) } | {array[i][5] + ' '*(HighestLength(array, 5) - Length(array[i][5])) }")

def printRapihF09(array, i, j):
    print(f"{j}. {array[i][0]}  | {array[i][1] + ' '*(HighestLength(array, 1) - Length(array[i][1])) } | {array[i][2] + ' '*(HighestLength(array, 2) - Length(array[i][2])) } | {array[i][3] + ' '*(HighestLength(array, 3) - Length(array[i][3])) } | {array[i][4] + ' '*(HighestLength(array, 4) - Length(array[i][4])) }")

def printRapihF10(array,i,j):
    print(f"{j}. {array[i][0]}  | {array[i][1] + ' '*(HighestLengthF10(array, 1) - Length(array[i][1])) } | {array[i][4] + ' '*(HighestLengthF10(array, 4) - Length(array[i][4])) } | {array[i][2] + ' '*(HighestLengthF10(array, 2) - Length(array[i][2])) } | {array[i][3] + ' '*(HighestLengthF10(array, 3) - Length(array[i][3]))}")

def printRapihF11(array,i,j):
    print(f"{j}. {array[i][0]}  | {array[i][1] + ' '*(HighestLengthF10(array, 1) - Length(array[i][1])) } | {array[i][4] + ' '*(HighestLengthF10(array, 4) - Length(array[i][4])) } | {array[i][2] + ' '*(HighestLengthF10(array, 2) - Length(array[i][2])) } | {array[i][3] + ' '*(HighestLengthF10(array, 3) - Length(array[i][3])) } | {array[i][-1] + ' '*(HighestLengthF10(array, -1) - Length(array[i][-1])) }")

def printRapihF13(array, i, j):
    print(f"{j}. {array[i][0]}  | {array[i][1] + ' '*(HighestLength(array, 1) - Length(array[i][1])) } | {array[i][2] + ' '*(HighestLength(array, 2) - Length(array[i][2])) } | {array[i][-1] + ' '*(HighestLength(array, -1) - Length(array[i][-1])) } |")