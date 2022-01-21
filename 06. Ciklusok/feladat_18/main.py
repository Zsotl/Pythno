szamokMennyisege: int = 0
osszeg: int = 0

print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek +1, 1):
        szamokMennyisege += 1

        if(szamokMennyisege % 2 == 1):
            osszeg += i
        if(szamokMennyisege % 2 == 0): 
            osszeg -= i 

print(f"Az összeg {osszeg}")
