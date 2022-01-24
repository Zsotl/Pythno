import time
import os

def hibaUzenet(text: str) -> None:
    print(text)
    time.sleep(3)
    os.system("cls")

#szam bekerese

def pontBekeres() -> int:
    pontszam: int = None
    while(pontszam == None):
        data: str = input("Kérem adja meg a pontszámot (0-100): ")
        if(data.isdigit()):
            pontszam: int = int(data)
            if(pontszam > 100 or pontszam < 0):
                hibaUzenet("0 és 100 között adjon meg!")
                pontszam = None
            else:
                return pontszam
        else:
            hibaUzenet("Számot adjon meg")
    

#szam vizsgalata
def pontVizsgalat(pontszam: int) -> int:
    if(pontszam < 50):
        return 1
    elif(pontszam >= 50 and pontszam < 60):
        return 2
    elif(pontszam >= 60 and pontszam < 70):
        return 3
    elif(pontszam >= 70 and pontszam < 85):
        return 4
    elif(pontszam >= 85):
        return 5
    
#kiiras
def kiiras(pontszam: int, jegy: int)-> None:
    print(f"Pontszáma: {pontszam} \nJegye: {jegy}")

#foprogram
pontszam: int = pontBekeres()
jegy: int = pontVizsgalat(pontszam)
kiiras(pontszam, jegy)