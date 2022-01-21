kisebb: int = None
nagyobb: int  = None
data: str = ""
lepesekSzama: int = None

while(kisebb == None):
    data = input("Kérem a kezdőértékét: ")
    if(data.replace("-", " ").isnumeric):
        kisebb = int(data)
    if(not data.isnumeric):
        print("Nem számot adott meg!")

while(nagyobb == None or nagyobb < kisebb):
    data = input("Kérem az előzőnél nagyobb végértéket: ")
    if(data.replace("-", " ").isnumeric):
        nagyobb = int(data)
    if(not data.isnumeric):
        print("Nem számot adott meg!")
    if(nagyobb < kisebb):
        print("Kisebb számot adott meg, mint a kezdőérték!")

while(lepesekSzama == None or lepesekSzama > nagyobb or lepesekSzama <= 0):
    data = input("Kérem a lépések számát: ")
    if(data.replace("-", " ").isnumeric):
        lepesekSzama = int(data)
    if(not data.isnumeric):
        print("Nem számot adott meg!")
    if(lepesekSzama <= 0):
        print("Túl alacsony számot adott meg!")
    if(lepesekSzama > nagyobb):
        print("Túl nagy számot adott meg!")

for i in range(nagyobb, kisebb - 1 , -lepesekSzama):
    print(i, end="  ")

