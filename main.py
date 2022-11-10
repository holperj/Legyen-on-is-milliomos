import random
from menu import menu, loggo_kiir
from beolvas import loadData


loggo_kiir()
osszesAdat = loadData()


def randomkerdes():
    x = random.choice(osszesAdat)
    osszesAdat.remove(x)
    if len(osszesAdat) == 0:
        print("Vége a játéknak.")
    else:
        if len(osszesAdat) > 7:
            
            print(f"{x.kerdes}")
            print(f"A, {x.valasz1}")
            print(f"B, {x.valasz2}")
            print(f"C, {x.valasz3}")
            print(f"D, {x.valasz4}")
            y = input("Írja be a válaszát: ")
            
                
    
valasz = -1
while valasz != 3:
    valasz = int(menu())
    if valasz == 1:
         print('Játék indítása')
         randomkerdes()
    elif valasz == 2:
        print('legjobb eredmény:')

    elif valasz == 3:
        print("A játéknak vége. A pontszámod: {}")
        





