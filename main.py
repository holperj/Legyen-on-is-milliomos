from jatek import jatekmenet
from menu import menu, loggo_kiir
from beolvas import loadData
from adatok import ertek


loggo_kiir()

valasz = -1
while valasz != 3:
    valasz = int(menu())
    if valasz == 1:
        print('Játék indítása')
        a = [True, 0]
        y = 0
        while a[0] != False and y != 3:
            a = jatekmenet()
            y += 1
        print(f"Vége a játéknak. \n Nyereményed: {ertek[a[1]]}")
        
    elif valasz == 2:
        print('legjobb eredmény:')

    elif valasz == 3:
        print(f"A játéknak vége.")






