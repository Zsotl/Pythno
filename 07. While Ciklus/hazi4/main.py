automataSzam: int = None
data: str = ""

while(automataSzam == None or automataSzam > 6 or automataSzam < 1):
    data = input("Melyik italt szeretné? \n Monster - 1\n Kávé - 2\n Icetea - 3\n Kóla - 4\n Red Bruh - 5\n")
    if(data.replace("-", " ").isnumeric):
        automataSzam = int(data)
    if(not data.isnumeric):
        print("Kérem számot adjon meg!")

if(automataSzam == 1):
    print("Itt az ön Monster-je")
if(automataSzam == 2):
    print("Itt az ön kávéja")
if(automataSzam == 3):
    print("Itt az ön icetea-ja")
if(automataSzam == 4):
    print("Itt az ön kólája")
if(automataSzam == 5):
    print("Nem xd ")
if(automataSzam > 5 or automataSzam < 0):
    print("Kérem az adott számok közül válasszon!")
