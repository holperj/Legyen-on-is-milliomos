from menu import menu

valasz = -1
while valasz != 3:
    valasz = int(menu())
    if valasz == 1:
        print('Játék indítása')
    elif valasz == 2:
        print('Eddigi eredmények:')
    # else:
    #     print('Nincs ilyen lehetőség, próbáld újra')