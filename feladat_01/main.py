"""
Töltsünk fel egy listát a felhasználó által megadott elemű random számokkal
"""

from typing import *
import random
import time
import os

halmaz: List[int] = []
elemekSzama: int = None
osszeg: int = None
ketJegyuSzamok: int = None

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

def halmazKiirasaForditva(kiirandoHalmaz: List[int]) -> None:
    for i in range(len(kiirandoHalmaz)-1, -1, -1):
        print(f"{kiirandoHalmaz[i]}", end="\t")

def parosSzamokKiirasa(kiirandoHalmaz: List[int]) -> None:
    for item in kiirandoHalmaz:
        if(item % 2 == 0):
            print(f"{item}", end="\t")

def sum(osszeadandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for item in osszeadandoHalmaz:
        eredmeny += item

    return eredmeny

def ketJegyuSzamokSzama(keresesHalmaza: List[int])-> int:
    eredmeny: int = 0
    for item in keresesHalmaza:
        if(abs(item) > 9 and abs(item) < 100):
            eremdeny += 1

    return eredmeny

#fopgrogram
elemekSzama = elemSzamBekeres() 
halmaz = listaFeltoltese(elemekSzama)

os.system("cls")
print("A halmaz elemei: \n")
halmazKiirasa(halmaz)
"""
1. feladat:  Írassuk ki a tartalmát fordított sorrendben
"""
print("\nA halmaz elemei fordítva: \n")
halmazKiirasaForditva(halmaz)

"""
2. feladat: Számítsuk ki az elemek összegét
"""

osszeg = sum(halmaz)
print(f"\nA halmaz elemeinek összege: {osszeg}")

"""
3. feladat: Átlagoljuk a tömbelemeket
"""

print(f"\nA halmaz elemeinek átlaga: {osszeg / elemekSzama}")

"""
4. feladat: írassuk ki a páros elemeket
"""

print(f"\nA halmaz páros elemei: ")
parosSzamokKiirasa(halmaz)

"""
5. feladat: Számoljuk meg, hogy hány két jegyű szám van a tömbben
"""
ketJegyuSzamok = ketJegyuSzamokSzama(halmaz)
print(f"\nA kétjegyű számok száma: {ketJegyuSzamok}")