from jatek import jatekmenet, osszesAdat
from menu import menu, loggo_kiir, menu_2
from beolvas import loadData, loaddata2, adatfelvetel, eredmeny, eredmeny_hozzaadas, search_by_name, kerdes_hozzaad, kerdes_felvetel
from adatok import ertek


loggo_kiir()
eredmeny = loaddata2()


valasz = -1
while valasz != 0:
    valasz = int(menu())
    if valasz == 1:
        print("-----------------------------------------")
        print('Játék indítása')
        a = ['', 0]
        y = 0      
        while a[0] != False and y != 15:
            print("-----------------------------------------")
            a = jatekmenet()
            if a[0] == True:
                y+=1
        print(f"Vége a játéknak. \n Nyereményed: {ertek[a[1]]}")
        print("-----------------------------------------")
        adat = adatfelvetel(a[1])
        eredmeny.append(adat)
        eredmeny_hozzaadas(adat)

    elif valasz == 2:
        valasz2 = -1
        while valasz2 != 0:
            valasz2 = int(menu_2())
            if valasz2 == 1:
                print("-----------------------------------------")
                print(f'Eredmények:\n')
                for item in eredmeny:
                    print(f"{item.nev} : {item.pont}Ft nyeremény.")

            elif valasz2 == 2:
                print("-----------------------------------------")
                nev = input('Adja meg a keresett nevet: ')
                talalt = search_by_name(eredmeny, nev)
                if talalt != False:
                    for item in talalt:
                        print("-----------------------------------------")
                        print(f'{item.nev} : {item.pont}Ft nyeremény.\n') 

    elif valasz == 3:
        adat = kerdes_felvetel()
        osszesAdat.append(adat)
        kerdes_hozzaad(adat)

    elif valasz == 0:
        print(f"A játéknak vége.")
        print("-----------------------------------------")






