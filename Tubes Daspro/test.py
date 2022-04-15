username = input("ID : ")

for i in username :
    if ( (ord(i) == 45) or (47 < ord(i) < 58) or (64 < ord(i) < 91) or (ord(i) == 95) or (96 < ord(i) < 123)):
        print(f"{i} = True")
    else:
        print(f"{i} = False")