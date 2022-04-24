password = input("Masukkan password: ")

# Affine Cipher
# rumus encrypt : (a*x + b)%m
# rumus decrypt : a*(x-b)%m 
# hubungan encrypt dan decrypty : (a encrypted) * (a * decrypted) % m = 1
# nilai b pada encrtpy dan decrypt bebas
# nilai x ialah tiap karakter dari password yang diencrypt/decrypt 
# nilai m ialah jumlah character yang bisa di cipher (ada 95 di code ascii)

encrypted = ''
for char in password:
    a = 1   
    b = 96
    m = 95
    x = ord(char) - 32  # -32 karena karakter ascii pada keyboaord di mulai dari code bernilai 32
    encrypt = chr(((a*x + b) % m) + 32) # +32 untuk mengembalikan lagi semula karena -32
    encrypted += encrypt

decrypted = ''
for char in encrypted:
    a = 96  
    b = 1
    m = 95
    x = ord(char) -32   # -32 karena karakter ascii pada keyboaord di mulai dari code bernilai 32
    decrypt = chr((a*(x - b) % m) + 32) # +32 untuk mengembalikan lagi semula karena -32
    decrypted += decrypt

print(f"Encrypted : {password} = {encrypted}")
print(f"Decrypted : {encrypted} = {decrypted}")