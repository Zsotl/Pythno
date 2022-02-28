from typing import *
import random

halmaz: List[int] = []
csakNegativHalmaz: List[int] = []
elemSzam: int = random.randint(10, 20)

def halmazFeltoltes(elemSzam: int) -> List[int]:
    eredmeny: List[int] = []
    for i in range(elemSzam):
        eredmeny.append(random.randint(-100, 100))

    return eredmeny

def csakNegativHalmazKeszites(halmaz: List[int])->List[int]:
    eredmeny: List[int] = []
    for szam in halmaz:
        if(szam < 0):
            eredmeny.append(szam)
    
    return eredmeny

def kiiras(halmaz: List[int], csakNegativHalmaz: List[int]) -> None:
    print("A halmaz pozitív elemei")
    for szam in halmaz:
        print(szam, end="\t")
    print("\nA halmaz negatív elemei")
    for szam2 in csakNegativHalmaz:
        print(szam2, end="\t")

halmaz = halmazFeltoltes(elemSzam)
csakNegativHalmaz = csakNegativHalmazKeszites(halmaz)
kiiras(halmaz, csakNegativHalmaz)
