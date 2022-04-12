import argparse, os

def load():
    global bisaLogin
    
    bisaLogin = False
    parser = argparse.ArgumentParser()
    parser.add_argument("folderName", nargs ="?")
    args = parser.parse_args()

    if not args.folderName:
        print("""Tidak ada nama folder yang diberikan!""")
        bisaLogin = False
        return False
    else:
        path = os.getcwd()  
        folderPath = os.path.join(path, args.folderName)
        if not os.path.exists(folderPath):    # Jika folderName tidak ada pada folderPath
            print(f'Folder "{args.folderName}" tidak ditemukan.\n')
            bisaLogin = False
            return False
        elif os.path.exists(folderPath):        # Jika folderName ada dan sama dengan folderPath
            print("Loading...\n")
            print('Selamat datang di antarmuka "Binomo"\n')
            bisaLogin = True
            return args.folderName

