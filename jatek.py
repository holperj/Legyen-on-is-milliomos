import random
from beolvas import loadData
osszesAdat = loadData()

def randomkerdes():
    x = random.choice(osszesAdat)
    osszesAdat.remove(x)
    if len(osszesAdat) == 0:
        print("Vége a játéknak.")
    else:
        if len(osszesAdat) > 7:
            print(f"{x.kerdes}")
            print(f"A, {random_valasz(x)}")
            print(f"B, {x.valasz2}")
            print(f"C, {x.valasz3}")
            print(f"D, {x.valasz4}")
            y = input("Írja be a válaszát: ")
                
def random_valasz(x):
    valaszok = []
    valaszok.append(x.kerdes1, x.kerdes2, x.kerdes3, x.kerdes4)
    A = random(1, 4)   
    a = valaszok(A)
    valaszok.remove(A)
    b = valaszok(B)
    valaszok.remove(B)
    c = valaszok(C)
    valaszok.remove(C)
    d = valaszok(1)
    valaszok.remove
    return a, b, c, d


