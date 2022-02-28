from typing import *
import random

fizetes: List[int] = []
honapok: Tuple[str] = (
    "Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December"
)
osszFizetes: int = None
szjaErteke: float = None
tbErtek: float = None
def fizetesGeneralas()-> List[int]:
    eredmeny: List[int] = []
    for i in range(12):
        eredmeny.append(random.randint(200, 1000))
    return eredmeny

def fizetesOsszege(fizetes: List[int])-> int:
    eredmeny: int = 0
    for szam in fizetes:
        eredmeny += szam
    return eredmeny

def szjaSzamolas()-> float:
    osszeg: int = fizetesOsszege(fizetes)
    return osszeg * 0.335

def TB(szja: float)-> float:
    return szja * 0.45 

def kiiras(honapok: Tuple[str], fizetes: List[int])-> None:
    for index in range(0, 12, 1):
        print(f"{honapok[index]} - {fizetes[index]} 000 HUF", end="\n")


fizetes = fizetesGeneralas()
kiiras(honapok, fizetes)
szjaErteke = szjaSzamolas()
tbErtek = TB(szjaErteke)
print(f"SZJA = {szjaErteke:1.1f} ezer HUF \nTB hozzájárulás: {tbErtek:1.1f} ezer HUF")
osszFizetes = fizetesOsszege(fizetes)
print(f"Éves fizetés: {osszFizetes}000 HUF")
