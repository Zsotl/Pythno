#I. szabály név nem lehet üres string
#II. szabály 1 vagy több szóköz
#III. szabály név hossza(minimum 3 karakter)
import time
import os

print("Kérem adja meg a nevét")
nev: str = str(input())

while(nev == "" or nev.isspace() or len(nev) < 3):
    if(nev == ""):
        print("Nem adta meg a nevét!")
        time.sleep(3)
        os.system("cls")
        nev = input("Adja meg a nevét újra!\n") 
    if(nev.isspace()):
        print("Ne csak szóközt adjon meg!")
        time.sleep(3)
        os.system("cls")
        nev = input("Adja meg a nevét újra!\n") 
    if(len(nev) < 3):
        print("Túl rövid a neve!")
        time.sleep(3)
        os.system("cls")
        nev = input("Adja meg a nevét újra!\n") 
print(f"Üdvözlöm, {nev}")

#hf 4. feladat