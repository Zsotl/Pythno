print("Kérem az első számot:")
x: float = float(input())

print("Kérem a számot amit ki szeretne vonni:")
y: float = float(input())

print("Kérem a számot amivel összeszorozná:")
z: float = float(input())

eredmeny: float = (x - y) * z
print(f"({x} - {y}) * {z} = {eredmeny}")