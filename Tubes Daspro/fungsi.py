def append(array1, array2):
    return array1 + array2

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

def printRapih(array):
    for i in range(1,Length(array)):
        print(f"{i}. {array[i][0]} | {array[i][1] + ' '*(HighestLength(array, 1) - Length(array[i][1])) } | {array[i][2] + ' '*(HighestLength(array, 2) - Length(array[i][2])) } | {array[i][3] + ' '*(HighestLength(array, 3) - Length(array[i][3])) } | {array[i][4] + ' '*(HighestLength(array, 4) - Length(array[i][4])) } | {array[i][5] + ' '*(HighestLength(array, 5) - Length(array[i][5])) }")