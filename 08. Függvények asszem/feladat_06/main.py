import random
import os
import time

start: int = None
end: int = None
titkos: int = None

# szam beolvasasa hatarertekek kozott

def szamBeolvasasa(kezdoErtek: int, vegErtek: int,) -> int:
    eredmeny: int = None
    while(eredmeny == None):
        data: str = input(f"Kérem adjon meg egy számot {kezdoErtek} - {vegErtek} között: ")
        if(data.isdigit and int(data) >= kezdoErtek and int(data) <= vegErtek):
            eredmeny: int = int(data)
            return eredmeny
        else:
            print("Nem jó a szám!")

elsoSzam = szamBeolvasasa(0, 9)
masodikSzam = szamBeolvasasa(40, 50)

#a kitalalando szam generalasa

def kitalalandoSzam(kezdoErtek: int, vegErtek: int,) -> int:
    randomSzam: int = random.randint(elsoSzam, masodikSzam + 1)
    return randomSzam
#Szam bekerese 

def tippBeolvasasa() -> int:
    eredmeny: int = None
    while(eredmeny == None):
        data: str = input(f"Kérem adjon meg egy tippet az előző lét száma között: ")
        if(data.isdigit()):
            return eredmeny

#kiiras sikeres tipp eseten

def sikeresTipp(tipp: int, probalkozasokSzama: int, szam: int) -> None:
    print(f"Próbálkozások száma: {probalkozasokSzama}.")
    print(f"A kitalálandó szám {szam} volt.")

#kiiras sikertelen tipp eseten

def sikertelenTipp(tipp: int, szam: int) -> None:
    if(tipp > szam):
        print("A kitalálandó szám kisebb")
    else:
        print("A kitalálandó szám nagyobb")

#tippek szamolasa
def jatek(szam: int) -> None:
    probalkozasokSzama: int = 0
    tipp: int = tippBeolvasasa()
    while(tipp != szam):
        if(tipp == szam):
            sikeresTipp(tipp, probalkozasokSzama, szam) #parametere
            probalkozasokSzama += 1
        else:
            sikertelenTipp(tipp, szam) #parameterek
            probalkozasokSzama += 1
        

#foprogram
start = elsoSzam
end = masodikSzam
titkos = kitalalandoSzam(start, end)

jatek(titkos)