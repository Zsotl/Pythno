import time
import os

atvaltottForint: float = None   
forint: float = None

def hiba(szoveg:str) -> None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def penzBekerese() -> float:
    eredmeny: float = None

    while(eredmeny == None):
        data:str = input("Kérem adjon meg egy kívánt értéket(forintban):")
        if(data.replace(".", "").isdigit()):
            eredmeny = float(data)
            return eredmeny
        else:
            hiba("Nem jó a bemenő adat!")

def valtasValasztas() -> str:
    eredmeny: str = None

    while(eredmeny == None):
        data:str = input("Kérem válassza ki a váltás módját:\n J: Japán jen\n S: Svájci frank\n A: Amerikai dollár \n")
        if(data.capitalize() == "J" or data.capitalize() == "A" or data.capitalize() == "S"):
            eredmeny = data.capitalize()
            return eredmeny
        else:
            hiba("Ilyen opció nincs!")

def atvaltas(forint: float, mire: str, forintEurora: float) -> float:
    forintEurora: float = forint / 356.75
    if(mire == "A"):
        return forintEurora * 0.8
    elif(mire == "S"):
        return forintEurora * 0.55
    elif(mire == "J"):
        return  forintEurora * 0.75

def kiiras(forint: float, atvaltottForint: float, penznem:str) -> None:
    print(f"{atvaltottForint} {penznem} = {forintEurora} EUR")

forint: float = penzBekerese()
penznem = valtasValasztas()
atvaltottForint = atvaltas(forint, penznem, forintEurora)
kiiras(forintEurora, atvaltottForint, penznem)