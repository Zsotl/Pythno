paratlanSzamokAmikOszthatoHarommal: int = 0

print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    if(i % 2 == 1 and i % 3 == 0):
        paratlanSzamokAmikOszthatoHarommal += 1

print(f"{paratlanSzamokAmikOszthatoHarommal} mennnyiségű páratlan 3-mal osztható szám van az intervallumban")