eletKor: str = ""
data: str = ""

while(eletKor == "" or eletKor > 100):
    data = input("Adja meg az életkorát: ")
    if(data.replace("-", " ").isnumeric):
        eletKor = int(data)
    if(eletKor > 99 or eletKor < 0):
        print("Reális életkort adjon meg!")
    if(not data.isnumeric):
        print("Számot adjon meg!")

if(eletKor < 7 and eletKor > 0):
    print("Maga egy gyerek")
if(eletKor < 19 and eletKor > 6):
    print("Maga egy iskolás")
if(eletKor < 66 and eletKor > 18):
    print("Maga egy dolgozó")
if(eletKor < 100 and eletKor > 64):
    print("Maga egy nyugdíjas")