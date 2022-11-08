import random
from menu import menu
from beolvas import loadData



adat = loadData()
adatok = []
for item in adat:
    adatok.append(item.kerdes)


kerdesek = []
kerdesek.append(adatok)


def randomkerdes():
    x = random.choice(adatok)
    adatok.remove(x)
    if len(adatok) == 0:
        print("Vége a játéknak.")
        
    print(f"A kérdés: {x}")




valasz = -1
while valasz != 3:
    valasz = int(menu())
    if valasz == 1:
         print('Játék indítása')
         randomkerdes()
         valasz == 3
         
    elif valasz == 2:
        print('Eddigi eredmények:')

    elif valasz == 3:
        print("A játéknak vége. A pontszámod: {}")
        break


