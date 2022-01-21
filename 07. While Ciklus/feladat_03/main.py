import random

rnd: int = random.randint(0 , 50)
probakSzama: int = 1
proba: int = 0
temp: str = ""

while( proba != rnd and probakSzama <= 5):

    temp = ""

    while(temp == "" or temp.isspace() or not temp.isnumeric):
        temp = input(f"Kérem az {probakSzama}. tippet: ")
        if(temp.isnumeric()):
            proba = int(temp)
            probakSzama += 1
        else: 
            print("Nem számot adott meg tippnek")

if(proba == rnd):
    print(f"Gratulálunk, eltalálta a számot ami {rnd} volt, ez {probakSzama} próbába telt")
else:
    print(f"Sajnos nem találta el a(z) {rnd} számot")