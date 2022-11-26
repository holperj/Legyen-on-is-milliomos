def menu():
    option = -1
    while option < 0 or option > 3:
        print("-----------------------------------------")
        print('1 - Játék')
        print('2 - Eredmények')
        print('3 - Kérdés hozzáadása')
        print('0 - Kilépés')
        print("-----------------------------------------")
        option = int(input('Válasszon a fentiek közül: '))
    return option

def loggo_kiir():
    file = open("logo.txt","r",encoding="utf-8")
    
    for row in file:
        print(row.strip('\n'))
    file.close

def menu_2():
    option = -1
    while option < 0 or option > 2:
        print("-----------------------------------------")
        print('1 - Összes eredmény')
        print('2 - Keresés az eredmények között')
        print('0 - Vissza')
        print("-----------------------------------------")
        option = int(input('Válasszon a fentiek közül: '))
    return option