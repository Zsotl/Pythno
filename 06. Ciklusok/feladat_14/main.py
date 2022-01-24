ottelOszthatoSzamok: int = 0
hettelOszthatoSzamok: int = 0

print("kérem az intervallum kezdetét:")
kezdoErtek: int = int(input())

print("kérem az intervallum végét:")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1 , 1):
    if(i % 5 == 0):
        ottelOszthatoSzamok += i

    if(i % 7 == 0):
        hettelOszthatoSzamok += i
    
if(ottelOszthatoSzamok > hettelOszthatoSzamok):
    print("Az öttel osztható számok összege nagyobb")
elif(hettelOszthatoSzamok > ottelOszthatoSzamok):
    print("A héttel osztható számok összege nagyobb")
elif(ottelOszthatoSzamok == hettelOszthatoSzamok):
    print("A két számmal osztható számok összege egyenlő")