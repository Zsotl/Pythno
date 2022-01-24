import os

data: str = ""
number: int = 0
osszeg: int = 0
probakSzama: int = 0

while(osszeg < 100):
    data = input("Kerem a szamot:")
    if(data.isnumeric()):
        number = int(data)
        osszeg += number
        probakSzama += 1
        print(F"Az eddigi számok összege: {osszeg}, próbálkozások száma {probakSzama}")
    else:
        print("A számok összege vagy nem egyenlő 100-al vagy nem számot adott meg")
        probakSzama += 1
print(f"A végső érték {osszeg}, próbálkozások száma {probakSzama}")
