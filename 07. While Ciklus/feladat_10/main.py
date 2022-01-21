n: int = None
data: str = ""
ottelOszthato: int = 0
tizeneggyelOszthato: int = 0

while(n == None or n < 0 or n > 99):
    data = input("Adjon meg egy kétjegyű számot: ")
    if(data.replace("-", " ").isnumeric()):
        n = int(data)
    if(not data.isnumeric()):
        print("Számot adjon meg!")
    if(n < 0 or n > 99):
        print("Maximum kétjegyű számot adjon meg")

for i in range(0, n + 1, 1):
    if(i % 2 == 0):
        print(i, end= "     ")
    if(i % 5 == 0):
        ottelOszthato += i
    if(i % 11 == 0):
        tizeneggyelOszthato += 1

print(f"\nAz öttel osztható számok összege {ottelOszthato}, a tizeneggyel osztható számok száma {tizeneggyelOszthato}")
print("A héttel osztott számok, melyeknek három a maradéka: ")
for i in range(0, n + 1, 1):
    if(i % 7 == 3):
        print(i, end= "     ")