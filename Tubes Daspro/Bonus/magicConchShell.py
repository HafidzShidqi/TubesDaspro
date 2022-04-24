import time

pertanyaan = input("Apa pertanyaanmu? ")

def hitungLength(pertanyaan):
    n = 0                   
    for i in pertanyaan:    
        n += 1
    return n                

x = hitungLength(pertanyaan)    

# Deklarasi fungsi lcg, yaitu proses linear congruential generator
# persamaan lcg : x1 = (a*x0 +c) % m
# nilai konstanta a (nilainya tidak akan berpengaruh pada hasil lcg)
# nilai konstanta m (nilainya tergantung dengan banyaknya output yang dihasilkan)
# nilai c sama dengan time.gmtime().tm_sec menghasilkan detik real time

def lcg(x):
    a = 10      
    m = 5       
    c = time.gmtime().tm_sec  
    x = (a * x + c ) % m        
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