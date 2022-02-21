from typing import *
import random

halmaz: List[int] = []
osszeg: int = None
atlag: float = None
elemSzam: int = random.randint(10,20)

def randomSzamHalmazFeltoltese(elemSzam: int) -> List[int]:
    eredmeny: List[int] = [] 
    szorzas: int = 1
    szam: int = 0
    for i in range(0, elemSzam, 1):
        szam: int = random.randint(100, 999)
        eredmeny.append(szam * szorzas)
        szorzas *= -1
    return eredmeny

def kiiras(halmaz: List[int]) -> None:
    for item in halmaz:
        print(f"{item}", end="\t")

def osszeadas(halmaz: List[int]) -> int:
    eredmeny: int = 0
    for item in halmaz:
        eredmeny += item
    return eredmeny

halmaz = randomSzamHalmazFeltoltese(elemSzam)
kiiras(halmaz)
osszeg = osszeadas(halmaz)
print(f"\nA randomszámok összege: {osszeg}")
print(f"\nA halmaz elemeinek átlaga: {osszeg / elemSzam}")