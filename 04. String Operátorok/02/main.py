from typing import*

text: str = "bonjour le monde"
textAsList: List[str] = text.split()

print(textAsList)

text: str = "Katarzyna Skoworonska Dolata; 190; center"
textAsList: List[str] = text.split(",")

print(textAsList)