parosSzamokOsszege: int = 0
paratlanSzamokSzorzata: int = 1

print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    if(i % 2 == 0):
        parosSzamokOsszege += i 
    else:
        paratlanSzamokSzorzata *= i

print(f"Páros számok összege {parosSzamokOsszege}, a páratlan számok szorzata {paratlanSzamokSzorzata}.")
