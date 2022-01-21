import os
import time

number: int = None
data: str = ""

while(number == None or number < 0 or number > 10):
    data = input("Kerem a szamot:")
    if(data.replace("-", "").isnumeric()):
        number = int(data)
    if(number != None or (number < 0 or number > 9)):
            print("\nNem 1 és 9 között van a szám(nincs 0 és 9 közt)!")
            time.sleep(3)
            os.system("cls")
    else: 
        print("\nNem számot írt be!")
        time.sleep(3)
        os.system("cls")      
                  
print(f"A beolvasott szám {number}")