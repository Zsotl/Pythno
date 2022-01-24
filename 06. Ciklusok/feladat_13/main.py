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
    
if(parosSzamokOsszege > paratlanSzamokOsszege):
    print(f"A {parosSzamokOsszege} nagyobb, mint {paratlanSzamokOsszege}")
elif(paratlanSzamokOsszege > parosSzamokOsszege):
    print(f"A {paratlanSzamokOsszege} nagyobb, mint {parosSzamokOsszege}")
else:
    print("A kettő összege egyenlő")