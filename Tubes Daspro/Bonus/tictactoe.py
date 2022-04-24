# Deklarasi fungsi inputGiliran yang memvalidasi input posisi x,y dari User

def inputGiliran():
    x = int(input("X: "))
    y = int(input("Y: "))
    while x > 3 or y > 3 or x < 1 or y < 1:
        print("Kotak tidak valid.\n")
        x = int(input("X: "))
        y = int(input("Y: "))
    return x,y

# Deklarasi procedure cetakPapan, yaitu mencetak ke layar status papan terkini
def cetakPapan():
    for i in range(3):
        for j in range(3):
            print(papan[i][j], end="")
        print()

# Deklarasi fungsi checkMenang, yaitu mengcheck kondisi menang jika terpenuhi
def checkMenang(Pemain):
    for i in range(3):
        if (papan[i][0] == papan[i][1] == papan[i][2] == Pemain):
            kondisi = 'horizontal'
            print(f'\n{Pemain} menang secara {kondisi}.')
            print(f"Kemenangan {kondisi} berlaku pada kolom lain")
            return True
        elif (papan[0][i] == papan[1][i] == papan[2][i] == Pemain):
            kondisi = 'vertikal'
            print(f'\n{Pemain} menang secara {kondisi}.')
            print(f"Kemenangan {kondisi} berlaku pada kolom lain")
            return True
        elif (papan[0][0] == papan[1][1] == papan[2][2] == Pemain) or (papan[2][0] == papan[1][1] == papan[0][2] == Pemain):
            kondisi = 'diagonal'
            print(f'\n{Pemain} menang secara {kondisi}.')
            print(f"Kemenangan {kondisi} berlaku pada {kondisi} yang sebaliknya.")
            return True

# Deklarasi fungsi checkTerisi, yaitu mengecheck apakah suatu kotak sudah terisi atau belum
def checkTerisi(x,y):
    if papan[y-1][x-1] != '#':
        return True
    else:
        return False

# Deklarasi matrix papan 3x3 of character
papan = [['#' for i in range(3)] for i in range(3)]

# Tampilan Awal
print("""
Legenda:
# Kosong
X Pemain 1
O pemain 2

Status Papan
###
###
###
""")

# Deklarasi variabel menang yang bernilai False
menang = False

# Deklarasi variabel i, sebagai penanda giliran ke-i
i = 0

# Melakukan looping selama belum menang
while not menang:
    if i % 2 == 0:  # Giliran Pemain X
        print('\nGiliran Pemain "X"')
        x,y = inputGiliran()    # Deklarasi x,y yaitu posisi kotak yang diinput oleh User
        while checkTerisi(x,y): # Mengecheck apakah posisi x,y sudah terisi atau belum
            print("Kotak sudah terisi. Silakan pilih kotak lain.")
            print('\nGiliran Pemain "X"')
            x,y = inputGiliran()    # Menginput lagi posisi x,y 
            checkTerisi(x,y)        # Dan check lagi apakah kotak x,y sudah terisi atau belum
        papan[y-1][x-1] = "X"       # Jika lolos dari pengecheckan, maka x,y dari papan akan terisi 'X'
        print("\nStatus Papan")
        cetakPapan()                # Menampilkan status papan terkini
        menang = checkMenang("X")   # Check apakah pemain X sudah menang atau belum
    else:           # Giliran Pemain O
        print('\nGiliran Pemain "O"')
        x,y = inputGiliran()    # Deklarasi x,y yaitu posisi kotak yang diinput oleh User
        while checkTerisi(x,y): # Mengecheck apakah posisi x,y sudah terisi atau belum
            print("Kotak sudah terisi. Silakan pilih kotak lain.")
            print('\nGiliran Pemain "O"')
            x,y = inputGiliran()    # Menginput lagi posisi x,y 
            checkTerisi(x,y)        # Dan check lagi apakah kotak x,y sudah terisi atau belum
        papan[y-1][x-1] = "O"       # Jika lolos dari pengecheckan, maka x,y dari papan akan terisi 'O'
        print("\nStatus Papan")
        cetakPapan()                # Menampilkan status papan terkini
        menang = checkMenang("O")   # Check apakah pemain O sudah menang atau belum

    i += 1          # Giliran bertambah 1 setelah Pemain X atau O telah mengisi kotak
    if i == 9:      # Jika kotak sudah terisi penuh dan belum ada yang menang
        print("Seri. Tidak ada yang menang.")
        menang = True   # Maka akan keluar looping dan mencetak bahwasanya permainan seri
    
