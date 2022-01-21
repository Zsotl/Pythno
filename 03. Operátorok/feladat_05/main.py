print("Kérem az első számot:")
x: float = float(input())

print("Kérem a számot amit hozzáadna:")
y: float = float(input())

osszeg: float = x + y 

print("Kérem a harmadik számot:")
z: float = float(input())

print("Kérem a számot amit kivonna a harmadikból:")
q: float = float(input())

kulonbseg: float = z - q

eredmeny: float = osszeg / kulonbseg

print(f"{osszeg} / {kulonbseg} = {eredmeny}")
