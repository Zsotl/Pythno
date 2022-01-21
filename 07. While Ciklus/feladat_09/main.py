szam: int = None
data: str = ""

while(szam == None or szam > 999 or szam < 100):
    data = input("Kérem adjon meg egy háromjegyű számot: ")
    if(data.replace("-", " ").isnumeric()):
        szam = int(data)
    if(not data.isnumeric()):
        print("Számot adjon meg!")
    if(szam > 1000 or szam < 100):
        print("Háromjegyű számot adjon meg!")

if(szam % 7 == 0):
    print(f"A száma {szam}, ez osztható héttel")
else:
    print(f"A száma {szam}, ez nem osztható héttel")