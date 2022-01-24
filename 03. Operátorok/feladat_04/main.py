print("Kérem az első számot:")
x: float = float(input())

print("Kérem a számot amivel megszorozná:")
y: float = float(input())

print("Kérem a számot amivel elosztaná az egészet:")
z: float = float(input())

eredmeny: float = (x * y) / z
print(f"({x} * {y}) / {z} = {eredmeny}")