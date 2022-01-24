takarekPenz: float = None
temp: str = ""
honapokSzama: int = 0

while(takarekPenz == None or takarekPenz > 50000 or takarekPenz < 10000):
    temp = input("Adja meg mennyi megtakarított pénze van(minimum 10000, maximum 50000): ")
    if(temp.isnumeric()):
        takarekPenz = float(temp)
    if(not temp.isnumeric()):
        print("Számot adjon meg!")
    if(takarekPenz > 50000):
        print("Túl nagy számot adott meg!")
    if(takarekPenz < 10000):
        print("Túl kicsi számot adott meg")
    
while(takarekPenz < 100000):
    takarekPenz = takarekPenz * 1.02
    honapokSzama += 1

print(f"A megtakarított pénze {honapokSzama} hónap alatt fog 100000 forintot érni")