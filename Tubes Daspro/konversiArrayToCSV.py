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
            if i < 4:
                stringKosong += str + ';'
                i += 1
            else:
                stringKosong += str
        stringKosong += '\n'

    return stringKosong

def KepemilikanArrayToCSV(lines):

    stringKosong = ''

    for line in lines:
        i = 0
        for str in line:
            if i < 1:
                stringKosong += str + ';'
                i += 1
            else:
                stringKosong += str
        stringKosong += '\n'

    return stringKosong
