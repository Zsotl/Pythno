harommalOszthatoSzamokSzama: int = 0

print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    if(i % 3 == 0):
        harommalOszthatoSzamokSzama += 1

print(f"Az intervallumban {harommalOszthatoSzamokSzama} darab 3-mal osztható szám van")