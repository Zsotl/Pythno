import time
import os

def nevBekeres() -> str:
    nev: str = None
    while(nev == None):
        temp: str = input("Kérem adja meg a nevét: ")
        if(len(temp) < 3):
            print("Túl rövid a neve!")
            time.sleep(3)
            os.system("cls")
        else:
            nev = temp

        return nev