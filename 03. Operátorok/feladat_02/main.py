print("Kérem az első számot:")
x: float = float(input())

print("Kérem a számot amit hozzáad:")
y: float = float(input())

print("Kérem a számot amit ezekből kivon:")
z: float = float(input())

eredmeny: float = (x + y) - z
print(f"({x} + {y}) -{z} = {eredmeny}")