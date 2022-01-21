print("Kérem adja meg hány elemű a számpiramis:")
piramisSzam: int = int(input())
segedSzam: int = piramisSzam

for i in range(piramisSzam, 0, -1):
    segedSzam -= 1
    for j in range(segedSzam, -1, -1):
        print(f"{j + 1}\t", end = " " )
    print("")