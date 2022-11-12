from jatek import jatekmenet
from menu import menu, loggo_kiir
from beolvas import loadData


loggo_kiir()

valasz = -1
while valasz != 3:
    valasz = int(menu())
    if valasz == 1:
        print('Játék indítása')
        a = ''
        while a != False:
            a = jatekmenet()

        print("Vége a játéknak.")
        
    elif valasz == 2:
        print('legjobb eredmény:')

    elif valasz == 3:
        print("A játéknak vége. A pontszámod: {}")






