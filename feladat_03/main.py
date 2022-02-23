from typing import *
import random

halmaz: List[int] = []
hatosDobasok: int = None
paratlanDobasok: int = None
dobasok : Dict[int, int] = {}
legtobbSzam: int = None 

def listaFeltoltese()-> List[int]:
    eredmeny: List[int] = []
    for item in range(7):
        eredmeny.append(random.randint(1, 6))
    return eredmeny

def kiiras(halmaz: List[int]) -> None:
    for item in halmaz:
        print(f"{item}", end="\t")
    
def hatosDobasokSzama(halmaz: List[int]) ->int:
    eredmeny: int = 0
    for i in halmaz:
        if(i % 6 == 0):
            eredmeny += 1
    return eredmeny

def paratlanDobasokSzama(halmaz: List[int]) -> int:
    eredmeny: int = 0
    for i in halmaz:
        if(i % 2 == 1):
            eredmeny += 1
    return eredmeny

def legtobbSzam(halmaz: List[int], dobasok: dict) -> int:
    eredmeny: int = 0
    if(dobasok.has_key("szam")):
    
    return eredmeny

halmaz = listaFeltoltese()
kiiras(halmaz)
hatosDobasok = hatosDobasokSzama(halmaz)
print(f"\n{hatosDobasok} db hatos számot dobtunk")
paratlanDobasok = paratlanDobasokSzama(halmaz)
print(f"\n{paratlanDobasok} db páratlan dobás volt")
legtobbSzam = legtobbSzam(halmaz, dobasok)
print(f"{legtobbSzam} volt legtöbbször")