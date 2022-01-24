print("Kérem az első számot:")
x: int = int(input())

print("Kérem a második számot:")
y: int = int(input())

if (x > y):
    print(f"{x} nagyobb mint {y}")
elif (x < y):
    print(f"{y} nagyobb mint {x}")
else:
    print("a két szám egyenlő")