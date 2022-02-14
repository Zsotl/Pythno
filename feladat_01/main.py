"""
Töltsünk fel egy listát a felhasználó által megadott elemű random számokkal
"""

from typing import *
import random
import time
import os

halmaz: List[int] = []
elemekSzama: int = None

def hiba(text: str) -> None:
    print(text)
    time.sleep(3)
    os.system("cls")

def elemSzamBekeres() -> int:
    eredmeny: int = None
    while(eredmeny == None):
        data: str = input("Kérem adja meg a halma elemeinek számát: ")
        if(data.isdigit()):
            eredmeny: int = int(data)
            if(eredmeny >= 2):
                return eredmeny
            else:
                hiba("1-nél nagyobb számot adjon meg!")
        else:
            hiba("Számot adjon meg")
#fopgrogram
elemSzama = elemSzamBekeres()