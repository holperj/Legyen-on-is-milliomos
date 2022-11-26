import random
from random import randint
from adatok import ertek
from beolvas import loadData

osszesAdat = loadData()

def jatekmenet():
    a = True
    x = 0
    y = 'konnyu'
    z = 'nehez'
    while a != False and x !=15:
        if x < 7:
            a = randomkerdes(y)
            if a == True:
                print(f"\nEddigi nyeremény: {ertek[x]}\n")
                print("-----------------------------------------")
                x += 1
        else: 
            a = randomkerdes(z)
            if a == True:
                print(f"\nEddigi nyeremény: {ertek[x]}\n")
                print("-----------------------------------------")
                x += 1
    return False, x

def kiir():
    for a in osszesAdat:
        print(f'{a.kerdes} - {a.nehezseg}')

def randomkerdes(nehezseg): 
    x = random.choice(osszesAdat)  
    while x.nehezseg != nehezseg:
        x = random.choice(osszesAdat)
    osszesAdat.remove(x)
    if len(osszesAdat) == 0:
        print("Vége a játéknak.")
    else:
        valaszok1, helyes = random_valasz(x)
        print(f"{x.kerdes}\n")
        print(f"A, {valaszok1[0]}")
        print(f"B, {valaszok1[1]}")
        print(f"C, {valaszok1[2]}")
        print(f"D, {valaszok1[3]}\n")
        y = ''
        valaszok = ['A', 'B', 'C', 'D']
        while y not in valaszok:
            y = input("Írja be a válaszát: ").upper()
            if y not in valaszok:
                print("Nincs ilyen választási lehetőség.")
            for i in range(len(valaszok)):
                if valaszok[i] == y:
                    if valaszok[i] != valaszok[helyes]:
                        return False
        return True

def random_valasz(x):
    valaszok = []
    helyes_index = ''
    helyes_valasz = x.valasz1
    valaszok.append(x.valasz1)
    valaszok.append(x.valasz2)
    valaszok.append(x.valasz3)
    valaszok.append(x.valasz4)
    valaszok_sorrendben = []
    valaszok_eredeti = valaszok
    for i in range(len(valaszok_eredeti)):
        a = randint(0, len(valaszok)-1)
        sor = valaszok[a]
        valaszok.remove(sor)
        valaszok_sorrendben.append(sor)
        if sor == helyes_valasz:
            helyes_index = i

    return valaszok_sorrendben, helyes_index
