intervallumAtlag:  int = 0
szamokMennyisege: int = 0

print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
        if(i % 1 == 0):
        intervallumAtlag += i
        szamokMennyisege += 1

atlag: float = intervallumAtlag / szamokMennyisege
print(f"A számok átlaga {atlag}")