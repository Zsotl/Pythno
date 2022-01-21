print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

if(kezdoErtek % 2 == 0):
    kezdoErtek + 1

for i in range(kezdoErtek, vegErtek, 2):
        print(i)
