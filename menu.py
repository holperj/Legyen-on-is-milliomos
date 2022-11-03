def menu():
    option = -1
    while option < 1 or option > 3: 
        print('1 - Játék')
        print('2 - Eredmények')
        print('3 - Kilépés')
        option = int(input('Válasszon a fentiek közül: '))
    return option

