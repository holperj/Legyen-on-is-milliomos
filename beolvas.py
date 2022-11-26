import random
from adatok import result, ertek, eredmeny

def loadData():
    results = []
    
    file = open("kerdesek.csv","r",encoding="utf-8")
    
    file.readline()
    
    for row in file:
        splitted = row.strip().split(";")
        res = result()
        res.kerdes = splitted[0]
        res.valasz1 = splitted[1]
        res.valasz2 = splitted[2]
        res.valasz3 = splitted[3]
        res.valasz4 = splitted[4]
        res.helyes = splitted[5]
        res.nehezseg = splitted[6]

        results.append(res)

    file.close()

    return results


def loaddata2():
    results = []
    
    file = open("eredmenyek.csv","r",encoding="utf-8")
    
    for row in file:
        splitted = row.strip().split(";")
        res = result()
        res.nev = splitted[0]
        res.pont = splitted[1]

        results.append(res)

    file.close()

    return results



def adatfelvetel(x):
    res = eredmeny()
    res.nev = input("Add meg a neved: ")
    res.pont = ertek[x]
    return res

def eredmeny_hozzaadas(res):
    file = open("eredmenyek.csv", "a", encoding= "utf-8")
    file.write(f"{res.nev};{res.pont} \n")
    file.close()


def search_by_name(results, name):
    eredmenytalalt = []
    for item in results:
        if item.nev == name:
            eredmenytalalt.append(item)
    if len(eredmenytalalt) == 0:
        print('\nNincs ilyen név\n')
        return False
    else: 
        return eredmenytalalt
    
def kerdes_felvetel():
    print('Új Kérdések megadása:')
    res = result()
    res.kerdes = input('Kérdés: ')
    res.valasz1 = input('1. Válasz (jó): ')
    res.valasz2 = input('2. Válasz: ')
    res.valasz3 = input('3. Válasz: ')
    res.valasz4 = input('4. Válasz: ')
    res.helyes = res.valasz1
    print("-----------------------------------------")
    print('1 - Könnyű')
    print('2 - Nehéz')
    print("-----------------------------------------")
    nehezseg = 0
    while nehezseg < 1 or nehezseg > 2:
        nehezseg = int(input(f'Adja meg a nehézséget:'))
        if nehezseg == 1:
            res.nehezseg = 'konnyu'
        elif nehezseg == 2:
            res.nehezseg = 'nehez'
    return res

def kerdes_hozzaad(res):
    file = open("kerdesek.csv", "a", encoding= "utf-8")
    file.write(f"{res.kerdes};{res.valasz1};{res.valasz2};{res.valasz3};{res.valasz4};{res.helyes};{res.nehezseg}\n")
    file.close()