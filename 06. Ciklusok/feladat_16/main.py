parosSzamokOsszege: int = 0
paratlanSzamokOsszege: int = 0

print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    if(i % 2 == 0):
        parosSzamokOsszege += i 
        
    else:
        paratlanSzamokOsszege += i
        
atlag: float = (parosSzamokOsszege + paratlanSzamokOsszege) / 2
print(f"A páros és a páratlan számok összegének átlaga {atlag}")