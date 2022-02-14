"""
Töltsünk fel egy listát a felhasználó által megadott elemű random számokkal
"""

from typing import *
import random
import time
import os

halmaz: List[int] = []
elemekSzama: int = None

def hiba(text: str) -> None:
    print(text)
    time.sleep(3)
    os.system("cls")

def elemSzamBekeres() -> int:
    eredmeny: int = None
    while(eredmeny == None):
        data: str = input("Kérem adja meg a halma elemeinek számát: ")
        if(data.isdigit()):
            eredmeny: int = int(data)
            if(eredmeny >= 2):
                return eredmeny
            else:
                hiba("1-nél nagyobb számot adjon meg!")
        else:
            hiba("Számot adjon meg")

def listaFeltoltese(elemekSzama: int) -> List[int]:
    eredmeny: List[int]=[]
    for i in range(elemekSzama):
        eredmeny.append(random.randint(-10, 10))
        time.sleep(0.001)
    return eredmeny

def halmazKiirasa(kiirandoHalmaz: List[int]) -> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")

"""
1. feladat:  Írassuk ki a tartalmát fordított sorrendben
"""
def halmazKiirasaForditva(kiirandoHalmaz: List[int]) -> None:
    for i in range(len(kiirandoHalmaz)-1, -1, -1):
        print(f"{kiirandoHalmaz[i]}", end="\t")
    

#fopgrogram
elemekSzama = elemSzamBekeres() 
halmaz = listaFeltoltese(elemekSzama)

os.system("cls")
print("A halmaz elemei: \n")
halmazKiirasa(halmaz)
print("\nA halmaz elemei fordítva: \n")
halmazKiirasaForditva(halmaz)
