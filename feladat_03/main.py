from typing import *
import random

halmaz: List[int] = []
hatosDobasok: int = None
paratlanDobasok: int = None
legtobbSzam: List[int] = {} 

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

def paratlanDobasokSzama(halmaz: List[int]) -> List[int]:
    eredmeny: int = 0
    for i in halmaz:
        if(i % 2 == 1):
            eredmeny += 1
    return eredmeny

def legnagyobbKulcsErteke(szotar: Dict[int, int]) -> List[int]:
    kulcs: int = None
    ertek: int = 0
    eredmeny: List[int] = []
    #a legnagyobb ertek kikeresese a szotarbol
    for key, value in szotar.items():#vegiglepkedunk a szotar osszes elemen kulcs-ertek parokkal
        if(szotar[key] > ertek):
            kulcs = key
            ertek = szotar[key]

    for key, value in szotar.items(): #kikeressuk azokat a  kulcsokat melyeknek az erteke egyenlo az ertek valtozoval, mivel azok a kulcsok(dobasok) szama fordul elo a legtobbszor
        if(szotar[key] == ertek):
            eredmeny.append(key)

    return eredmeny

def legtobbSzam(halmaz: List[int]) -> List[int]:
    szotar: Dict[int, int] = {} #Dict[kulcs -> szam, value -> szam elofordulasi szama]    
    #meghatarozzuk az elofordulasi szamokat
    
    for szam in halmaz:
        if(szam in szotar):
            szotar[szam] += 1 #a kulcshoz tartozo erteket adja vissza
        else:
            szotar[szam] = 1

    #lista = [2, 4, 1, 1, 6, 3, 5]
    eredmeny: List[int] = legnagyobbKulcsErteke(szotar)

    return eredmeny

halmaz = listaFeltoltese()
kiiras(halmaz)
hatosDobasok = hatosDobasokSzama(halmaz)
print(f"\n{hatosDobasok} db hatos számot dobtunk")
paratlanDobasok = paratlanDobasokSzama(halmaz)
print(f"{paratlanDobasok} db páratlan dobás volt")
legtobbSzam = legtobbSzam(halmaz)
print(f"{legtobbSzam} szerepelt legtöbbször")