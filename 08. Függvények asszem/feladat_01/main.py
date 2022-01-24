#1 - Írjunk programot amely összead, kivon, szoroz és eloszt két számot.
#A matematikai műveleteket függvényekkel oldjuk meg.
from matematikafuggvenyek import *
from inputLib import *

osszeg: float = None
kulonbseg: float = None
szorzat: float = None
hanyados: float = None

elsoSzam: float = None
masodikSzam: float = None

print("Adja meg az első számot: ")
elsoSzam = tizedesSzamBeolvasas()

print("Adja meg a második számot: ")
masodikSzam = tizedesSzamBeolvasas()

osszeg = osszeadas(elsoSzam, masodikSzam)
kulonbseg = kivonas(elsoSzam, masodikSzam)
szorzat = szorzas(elsoSzam, masodikSzam)
hanyados = osztas(elsoSzam, masodikSzam)

print(f"A két szám összege {osszeg}, kivonásuk {kulonbseg}, szorzatuk {szorzat}, hányadosuk {hanyados}")