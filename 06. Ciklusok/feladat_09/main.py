print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

if(vegErtek % 2 == 1):
    vegErtek -= 1

for i in range(vegErtek, kezdoErtek-1, -2):
        print(i)
