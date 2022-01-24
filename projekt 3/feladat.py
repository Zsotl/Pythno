import re
import time
import os

from typing import Dict

def isUserExists(email: str, password: str) -> bool:
    users: Dict[str, str] = {
        'hetfo@test.com': 'Testjelszo1',
        'kedd@test.com': 'Testjelszo2',
        'szerda@test.com': 'Testjelszo3',
        'csutortok@test.com': 'Testjelszo4',
        'pentek@test.com': 'Testjelszo5',
        'szombat@test.com': 'Testjelszo6',
        'vasarnap@test.com': 'Testjelszo7'
    }
    
    isExists: bool = ((email, password) in users.items())

    if(isExists == True):
        print("Sikeres bejelentkezés a rendszerbe!")
    else:
        print("A rendszerhez való hozzáférés megtagadva!")
    
    return isExists

regexEmail = re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
regexJelszo = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

email: str = None
jelszo: str = None
validJelszo: bool = None
validEmail: bool = None

def isValidEmail(email: str) -> bool:
    if re.fullmatch(regexEmail, email):
        return True
    else:
        return False

def isValidJelszo(jelszo: str) -> bool:
    if re.fullmatch(regexJelszo, jelszo):
        return True
    else:
        return False

while(validEmail == None or validEmail == False):
    data: str = input("Email-cím: ")
    validEmail: bool = isValidEmail(data)
    if(validEmail == True):
        email: str = str(data)
    else:
        print("Hibás email cím!")
        time.sleep(3)
        os.system("cls")

while(validJelszo == None or validJelszo == False):
    data: str = input("Jelszó: ")
    validJelszo: bool = isValidJelszo(data)
    if(validJelszo == True):
        jelszo: str = str(data)
    else:
        print("Hibás jelszó")
        time.sleep(3)
        os.system("cls")
