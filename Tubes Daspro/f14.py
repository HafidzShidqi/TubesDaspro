from f03 import *

def help(role):
    if role == "Admin":
        print("""
============ HELP ============
1. register - Untuk melakukan registrasi user baru
2. login - Untuk melakukan login ke dalam sistem
3. tambah_game - Untuk menambah game yang dijual pada toko
4. ubah_game - Untuk mengubah nama, kategori, tahun rilis, atau harga game yang dijual pada toko
5. ubah_stok - Untuk mengubah stok game yang dijual pada toko
6. list_game_toko - Untuk melihat list game yang dijual pada toko berdasarkan skema tahun rilis atau harga
7. search_game_at_store - Untuk mencari game pada toko dengan menginput 5 parameter yang bersifat tidak wajib
8. topup - Untuk menambah saldo kepada user
9. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
10. exit - Untuk keluar dari aplikasi
""")
    else:
        print("""
============ HELP ============
1. login - Untuk melakukan login ke dalam sistem
2. list_game_toko - Untuk melihat list game yang dijual pada toko berdasarkan skema tahun rilis atau harga
3. buy_game - Untuk membeli game (1 pengguna maksimal 1 game)
4. list_game - Untuk melihat daftar game yang dimiliki pengguna
5. search_my_game - Untuk mendapatkan informasi game yang dimiliki pengguna sesuai dengan query dari parameter yang diinput
6. search_game_at_store - Untuk mencari game pada toko dengan menginput 5 parameter yang bersifat tidak wajib
7. riwayat - Untuk melihat pembelian game dengan atribut (ID | Nama Game | Harga | Tahun Beli)
8. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
9. exit - Untuk keluar dari aplikasi
""")

