from jatek import jatekmenet
from menu import menu, loggo_kiir
from beolvas import loadData, loaddata2
from adatok import ertek, adatfelvetel, eredmeny, hozzaadas, search_by_name


loggo_kiir()
eredmeny = loaddata2()

valasz = -1
while valasz != 3:
    valasz = int(menu())
    if valasz == 1:
        print('Játék indítása')
        a = [True, 0]
        y = 0
        
        while a[0] != False and y != 3:
            print("-----------------------------------------")
            a = jatekmenet()
            y += 1
        print(f"Vége a játéknak. \n Nyereményed: {ertek[a[1]]}")
        print("-----------------------------------------")
        adat = adatfelvetel(a[1])
        eredmeny.append(adat)
        hozzaadas(adat)
    elif valasz == 2:
        print("-----------------------------------------")
        print(f'eredmények:')
        for item in eredmeny:
            print(f"{item.nev} : {item.pont}Ft nyeremény.")
        print("-----------------------------------------")
        nev = input('Adja meg a keresett nevet: ')
        talalt = search_by_name(eredmeny, nev)
        if talalt != False:
            for item in talalt:
                print(f'{item.nev} : {item.pont}Ft nyeremény.')
    elif valasz == 3:
        print(f"A játéknak vége.")
        print("-----------------------------------------")






