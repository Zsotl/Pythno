






import os
import time

celsius: float = None
atvaltasMertekegysege: str = None
atvaltottMennyiseg: float = None
def hibaUzenet(hiba: str) -> None:
    print("Készülj fel, mert most jönnek a testvérek éés elrabolunk.")
    time.sleep(3)
    os.system("cls")

#homerseklet bekerese celsiusban

def hoBekeres() -> float:
    eredmeny: float = None
    
    while(eredmeny == None):
        data: str = input("Kérem adja meg a hőmérsékletet Celsius-ban: ")
        if(data.replace("-", "").replace(".", "").isdigit()):
            eredmeny = float(data)
            return eredmeny
        else: 
            hibaUzenet("Készülj fel, mert most jönnek a testvérek éés elrabolunk.")

# F vagy K legyen a valtas modja

def valtasMod() ->  str: 
    eredmeny: str = None
    
    while(eredmeny == None):
        data: str = input("Kérem a váltás módját[F vagy K]: ")
        if(data.capitalize() == "K" or data.capitalize() == "F"):
            eredmeny = data.capitalize()
            return eredmeny
        else: 
            hibaUzenet("Készülj fel, mert most jönnek a testvérek éés elrabolunk.")

#atvaltas

def atvaltas(fokCelsius: float, mire: str) -> float: 
    if(mire == "K"):
        return fokCelsius + 273.15
    elif(mire == "F"):
        return 9 / 5 * fokCelsius + 32 

#kiiras

def kiiras(fokCelsius: float, atvaltottFok: float, mertekegyseg: str) -> None:
    print(f"{fokCelsius}C = {atvaltottFok}{mertekegyseg}")

#foprogram
celsius = hoBekeres()
atvaltasMertekegysege = valtasMod()
atvaltottMennyiseg = atvaltas(celsius, atvaltasMertekegysege)
kiiras(celsius, atvaltottMennyiseg, atvaltasMertekegysege)