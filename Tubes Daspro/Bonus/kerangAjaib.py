import time

# Deklarasi variabel pertanyaan, nilainya merupakan input dari user
pertanyaan = input("Apa pertanyaanmu? ")

# Deklarasi fungsi hitungLength, untuk menghitung panjang dari variabel pertanyaan
def hitungLength(pertanyaan):
    n = 0                   # Deklarasi nilai awal
    for i in pertanyaan:    # Iterasi untuk mendapatkan panjang dari variabel pertanyaan
        n += 1
    return n                # Meng-return hasilnya

x = hitungLength(pertanyaan)    # Deklarasi varibel x, yang memanggil fungsi hitungLength dan memiliki
                                # value dari panjang dari variabel pertanyaan

# Deklarasi fungsi lcg, yaitu proses linear congruential generator
def lcg(x):
    a = 10      # Deklarasi nilai konstanta a (nilainya tidak akan berpengaruh pada hasil lcg)
    m = 5       # Deklarasi nilai konstanta m (nilainya tergantung dengan banyaknya output yang dihasilkan)
    c = time.gmtime().tm_sec    # time.gmtime().tm_sec menghasilkan detik real time
    x = (a * x + c ) % m        # Persamaan lcg yang menghasilkan random number
    return x    # Meng-return hasil bilangan 0-4 secara acak

# Pengecheckan nilai fungsi yang dihasilkan lcg(x) dan menghasilkan output 
if lcg(x) == 0:
    print('Iya')
elif lcg(x) == 1:
    print('Bukan')
elif lcg(x) == 2:
    print('Mungkin')
elif lcg(x) == 3:
    print('Bisa Jadi')
elif lcg(x) == 4:
    print('YNTKTS')