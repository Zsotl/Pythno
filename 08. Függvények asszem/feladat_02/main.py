import time
import os

def nevBekeres() -> str: 
    nev: str = None
    while(nev == None):
        data: str = input("Kérem a nevét: ")

        if(len(data) < 3): #megszámolja a karaktereket
            print("Túl rövid a neved bocs tesom, minimum 3 karakter")
            time.sleep(3)
            os.system("cls")
        else:
            nev = data

    return nev

def udvozles(nev: str) -> None:
    print(f"Szia {nev}.")

felhasznalo : str = nevBekeres()
udvozles(felhasznalo)