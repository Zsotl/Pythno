import datetime
import time
import os


#nev bekerese, szuletesi ev bekerese, kiiratas, eletkor kiszamolasa

felhasznaloNev: str = None
kor: int =  None

def nevBekeres() -> str:
    nev: str = None
    while(nev == None):
        temp: str = input("Kérem adja meg a nevét: ")
        if(len(temp) < 3):
            print("Túl rövid a neve!")
            time.sleep(3)
            os.system("cls")
        else:
            nev = temp

        return nev

def szuletesBekeres() -> int:
    szuletesiEv: int = None
    ma: datetime = datetime.datetime.now()
    jelenlegiEv: int = int(ma.strftime("%Y")) #visszadja a jelenlegi évet a változóból
    while(szuletesiEv == None):
        temp: str = input("Kérem adja meg melyik évben született: ")
        if(temp.replace("-", "").isnumeric):
                szuletesiEv: int(data)
        if(szuletesiEv >= jelenlegiEv):
            szuletesiEv = None
            print("Még csak 2022 van!")
            time.sleep(3)
            os.system("cls")
        return szuletesiEv

def eletkorSzamolas(szuletesiEv: int) -> int: 
    ma: datetime = datetime.datetime.now()
    jelenlegiEv: int = int(ma.strftime("%Y"))
    eletkor: int = jelenlegiEv - szuletesiEv

    return eletkor-szuletesiEv

def kiiratas(nev: str, ev: int) ->  None:
    print(f"{nev}, ön {kor} éves.")

felhasznaloNev = nevBekeres()
szuletesiEv = szuletesBekeres()
kor = eletkorSzamolas(szuletesiEv)
kiiratas(felhasznaloNev, kor)