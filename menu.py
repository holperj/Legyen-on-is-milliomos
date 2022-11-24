def menu():
    option = -1
    while option < 1 or option > 3:
        print("-----------------------------------------")
        print('1 - Játék')
        print('2 - Eredmények')
        print('3 - Kilépés')
        print("-----------------------------------------")
        option = int(input('Válasszon a fentiek közül: '))
    return option

def loggo_kiir():
    file = open("logo.txt","r",encoding="utf-8")
    
    for row in file:
        print(row.strip('\n'))
    file.close
