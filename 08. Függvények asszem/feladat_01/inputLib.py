import time
import os

def tizedesSzamBeolvasas() -> float:
    szam: float = None
    while(szam == None):
        data: str = input()
        if(data.replace("-", "").replace(".", "").isnumeric()):
            szam = float(data)
            return szam
        else:
            print("Számot adjon meg!")
            time.sleep(3)
            os.system("cls")
