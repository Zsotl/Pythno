print("kérem az első számot:")
x: int = int(input())

print("kérem a második számot:")
y: int = int (input())

print("kérem a harmadik számot:")
z: int = int (input())

if(x > y and x > z and y > z):
    print(f"{z},{y},{x}")
elif(x > y and x > z and z > y):
     print(f"{y},{z},{x}")
elif((x > y or x == y) and (x > z or x == z)):
     nagyobbSzam: int = x
     print(f"{y}, {z}, {nagyobbSzam}")

if(y > x and y > z and x > z):
    print(f"{z},{x},{y}")
elif(y >x and y > z and z > x):
     print(f"{x},{z},{y}")
elif((y > x or y == x) and (y > z or y == z)):
     nagyobbSzam: int = y
     print(f"{x}, {z}, {nagyobbSzam}")

if(z > x and z > y and x > y):
     print(f"{y},{x},{z}")
elif(z > x and z > y and y > x):
     print(f"{x},{y},{z}")
elif((z > x or z == x) and (z > y or z == y)):
     nagyobbSzam: int = z
     print(f"{y}, {x}, {nagyobbSzam}")

























































