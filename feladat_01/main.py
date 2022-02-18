"""
Töltsünk fel egy listát a felhasználó által megadott elemű random számokkal
"""

from typing import *
import random
import time
import os

max: int = None
min: int = None
halmaz: List[int] = []
elemekSzama: int = None
osszeg: int = None
ketJegyuSzamok: int = None
egyjegyuSzamok: int = None
paratlanSzamokOsszege: int = None
nullaraVegzodoSzamokOsszege: int = None
novekvoHalmaz: int = None

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
            eredmeny += 1

    return eredmeny

def egyjegyuSzamokSzama(kiirandoHalmaz: List[int])-> int:
    eredmeny: int = 0
    for item in kiirandoHalmaz:
        if(abs(item) < 10):
            print(f"{item}", end="\t")

    return eredmeny

def paratlanSzamokOsszege(keresesHalmaza: List[int])-> int:
    eredmeny: int = 0
    for item in keresesHalmaza:
        if(item % 2 == 1):
            eredmeny += item
    return eredmeny

def nullaraVegzodoSzamokSzama(keresesHalmaza: List[int]) -> int:
    eredmeny: int = 0
    for item in keresesHalmaza:
        if(item % 10 == 0):
            eredmeny += 1
    return eredmeny

def novekvoSorrend(keresesHalmaza: List[int]) -> List[int]:
    temp: int = None
    for i in range (0, len(keresesHalmaza), 1):
        for j in range(i + 1, len(keresesHalmaza), 1):
            if(keresesHalmaza[j] < keresesHalmaza[i]):
                temp = keresesHalmaza[i]
                keresesHalmaza[i] = keresesHalmaza[j]
                keresesHalmaza[j] = temp

    return keresesHalmaza

def legnagyobbSzamKereses(keresesHalmaza: List[int]) -> List[int]:
    max: int = keresesHalmaza[0]
    for index in range (1, len(keresesHalmaza)):
        if(keresesHalmaza[index] > max):
            max = keresesHalmaza[index]
    return max

def legkisebbSzamIndexe(keresesHalmaza: List[int]) -> int:
    index: int = 0
    min: int = keresesHalmaza[index]
    for i in range (1, len(keresesHalmaza)):
        if(keresesHalmaza[i] < min):
            min = keresesHalmaza[i]
            index = i
    return index

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

"""
6. feladat: Írassuk ki az egyjegyű számokat
"""
print("\nA halmaz egyjegyű elemei: ")
egyjegyuSzamokSzama(halmaz)

"""
7. feladat: Számítsuk ki a páratlan számok összegét
"""
paratlanSzamokOsszege = paratlanSzamokOsszege(halmaz)
print(f"\nA halmaz páratlan számú elemeinek összege: {paratlanSzamokOsszege}")

"""
8. feladat: Számoljuk meg hány nullára végződő szám van a tömbben
"""
nullaraVegzodoSzamokOsszege = nullaraVegzodoSzamokSzama(halmaz)
print(f"\nA halmazban {nullaraVegzodoSzamokOsszege} db nullára végződő szám van")
"""
9. feladat: Rakjuk sorba a listát növekvő/csökkenő sorrendbe

novekvoHalmaz = novekvoSorrend(halmaz)
print(f"\nA halmaz növekvő sorrendben: {novekvoHalmaz}")
"""
"""
10. feladat: Keressük ki a legnagyobb számot
"""
max = legnagyobbSzamKereses(halmaz)
print(f"\nA legnagyobb szám {max}")
"""
11. feladat: Keressük ki a legkisebb szám indexét
"""
min = legkisebbSzamIndexe(halmaz)
print(f"\nA legkisebb szám {min}. helyen helyezkedik el")