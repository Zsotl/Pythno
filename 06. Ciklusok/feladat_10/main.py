sum: int = 0
szorzat: int = 1

print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    sum += i
    szorzat *= i

print(f"A számok szorzata {szorzat}, összegük {sum}")