from typing import *
import random

halmaz1: List[int] = []
halmaz2: List[int] = []
elemSzam1: int = None
elemSzam2: int = None
nagyHalmaz: List[int] = []
novekvoHalmaz: List[int] = []

def szamBekeres() -> int:
    eredmeny: int = None
    while(eredmeny == None):
        data: str = input("Adja meg az első lista elemeinek számát(1 - 5): ")
        if(data.isdigit):
            eredmeny: int = int(data)
            if(eredmeny < 1 or eredmeny > 5):
                print("Nem jó szám !")
                eredmeny = None
            else:
                return eredmeny
        else:
            print("Számot adj meg!")    
        
def szamBekeres2() -> int:
    eredmeny: int = None
    while(eredmeny == None):
        data: str = input("Adja meg az második lista elemeinek számát(6- 10): ")
        if(data.isdigit):
            eredmeny: int = int(data)
            if(eredmeny < 6 or eredmeny > 10):
                print("Nem jó szám!")
                eredmeny = None
            else:
                return eredmeny
        else:
            print("Számot adj meg!")    
        
def halmaz1Feltoltes(elemSzam1: int) -> List[int]:
    eredmeny: List[int] = []
    for i in range(elemSzam1):
        eredmeny.append(random.randint(1, 10))
    return eredmeny

def halmaz2Feltoltes(elemSzam2: int) -> List[int]:
    eredmeny: List[int] = []
    for i in range(elemSzam2):
        eredmeny.append(random.randint(1, 10))
    return eredmeny

def novekvoSorrend(nagyHalmaz: List[int]) -> List[int]:
    data: int = None
    for i in range (0, len(nagyHalmaz), 1):
        for j in range(i + 1, len(nagyHalmaz), 1):
            if(nagyHalmaz[j] < nagyHalmaz[i]):
                data = nagyHalmaz[i]
                nagyHalmaz[i] = nagyHalmaz[j]
                nagyHalmaz[j] = data
    return nagyHalmaz

def halmazAtlaga(nagyHalmaz: List[int])-> float:
    eredmeny: float = None
    

elemSzam1 = szamBekeres()
elemSzam2 = szamBekeres2()
halmaz1 = halmaz1Feltoltes(elemSzam1)
halmaz2 = halmaz2Feltoltes(elemSzam2)
nagyHalmaz = halmaz1 + halmaz2
print(f"A számok: {nagyHalmaz}")
novekvoHalmaz = novekvoSorrend(nagyHalmaz)
print(F"A számok növekő sorrendben: {novekvoHalmaz}")