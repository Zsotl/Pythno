hatarErtek: int = 0
probak: int = 0
data: str = ""
szamokOsszege: int = 0
szamInput: str = ""

while(szamokOsszege == "" or hatarErtek < 100):
    data = input("Kérem a végértéket:")
    if(data.replace("-", " ").isnumeric()):
        hatarErtek = int(data)
    if(hatarErtek < 100):
        print("100-nál kisebb értéket adott meg")
        probak += 1
    if(not data.isnumeric):
        print("Számot adjon meg!")
        probak += 1 

while(hatarErtek > szamokOsszege):
    szamInput = input("Kérek egy számot:")
    if(szamInput.replace("-", " ").isnumeric):
        szam = int(szamInput)
        szamokOsszege += szam
        probak += 1
print(f"A végső érték {szamokOsszege}, próbák száma {probak}")