import random

kezdoErtek: int = None
vegErtek: int = None
data: str = ""
neggyelOszthato: int = 0

while(kezdoErtek == None or vegErtek == None or kezdoErtek > vegErtek):
    data = input("Kérem adjon meg egy páros számot: ")
    if(data.replace("-", "").isnumeric()):
        kezdoErtek = int(data)
        if(kezdoErtek % 2 == 1):
                print("Páros számot adjon meg!")
        if(kezdoErtek < 0):
            print("Pozitív számot adjon meg!")
        if(not data.isnumeric()):
            print("Számot adjon meg!")
    data = input("Kérem adjon meg egy páratlan számot, mely nagyobb mint az előző érték: ")
    if(data.replace("-", " ").isnumeric()):
        vegErtek = int(data)
        if(vegErtek % 2 == 0):
            print("Ne páros számot adjon meg!")
        if(kezdoErtek > vegErtek):
            print("Kisebb értéket adott meg mint a kezdőérték!")
        if(not data.isnumeric):
            print("Számot adjon meg!")
    if(vegErtek < 0):
        print("Pozitív számot adjon meg!")
randomSzam: int = random.randint(kezdoErtek, vegErtek)

if(abs(randomSzam - kezdoErtek) < abs (randomSzam - vegErtek)):
    print(f"A {kezdoErtek} közelebb volt a random számhoz, ami a {randomSzam} volt")
elif(abs (randomSzam - kezdoErtek) > abs (randomSzam - vegErtek)):
    print(f"A {vegErtek} közelebb volt a random számhoz, ami a {randomSzam} volt")
else:
    print(f"A két szám egyenlő távolságra van a random számtól, ami {randomSzam} volt")

atlag: float = (kezdoErtek + vegErtek)/2

for i in range(kezdoErtek, vegErtek + 1, 1):
    if(i % 4 == 0):
        neggyelOszthato += 1
print(f"A számok átlaga {atlag}, {neggyelOszthato} db 4-gyel osztható szám volt a két érték között")