print("Kérem az első számot:")
x: float = float(input())

print("Kérem a második számot:")
y: float = float(input())

szorzas: float = x * 0.5

kivonas: float = y - 0.7

print("Kérem a harmadik számot:")
z: float = float(input())

eredmeny: float = (szorzas * kivonas) % z
print(f"({szorzas} * {kivonas} % {z} = {eredmeny}")
