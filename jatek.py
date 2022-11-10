import random
from random import randint
from beolvas import loadData
osszesAdat = loadData()

def randomkerdes():
    x = random.choice(osszesAdat)
    osszesAdat.remove(x)
    if len(osszesAdat) == 0:
        print("Vége a játéknak.")
    else:
        if len(osszesAdat) > 7:
            a, b, c, d = random_valasz(x)
            print(f"{x.kerdes}")
            print(f"A, {a}")
            print(f"B, {b}")
            print(f"C, {c}")
            print(f"D, {d}")
            y = input("Írja be a válaszát: ").upper
    return y, a, b, c, d

def random_valasz(x):
    valaszok = []
    valaszok.append(x.valasz1)
    valaszok.append(x.valasz2)
    valaszok.append(x.valasz3)
    valaszok.append(x.valasz4)
    A = randint(0, 3)   
    a = valaszok[A]
    valaszok.remove(a)
    B = randint(0, 2)
    b = valaszok[B]
    valaszok.remove(b)
    C = randint(0, 1)
    c = valaszok[C]
    valaszok.remove(c)
    d = valaszok[0]
    return a, b, c, d

def valasz_elfogad():
    y, a, b, c, d = randomkerdes()
