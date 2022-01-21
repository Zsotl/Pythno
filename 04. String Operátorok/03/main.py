from typing import*

text: str = "bonjour le monde"
index: int = text.find("on") #balról
indexRight: int = text.rfind("on") #jobbról duh

print(index)
print(indexRight)