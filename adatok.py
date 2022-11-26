class result:
    kerdes = ""
    valasz1 = ""
    valasz2 = ""
    valasz3 = ""
    valasz4 = ""
    helyes = ""
    nehezseg = ""

class eredmeny:
    nev = ""
    pont = ""



ertek = [
"0",
"10 000",
"20 000",
"50 000",
"100 000",
"250 000",
"500 000",
"750 000",
"1 000 000",
"1 500 000",
"2 000 000",
"5 000 000",
"10 000 000",
"15 000 000",
"25 000 000",
"50 000 000"]


def adatfelvetel(x):
    res = eredmeny()
    res.nev = input("Add meg a neved: ")
    res.pont = ertek[x]
    return res

def hozzaadas(res):
    file = open("eredmenyek.csv", "a", encoding= "utf-8")
    file.write(f"{res.nev};{res.pont} \n")
    file.close()


def search_by_name(results, name):
    eredmenytalalt = []
    for item in results:
        if item.nev == name:
            eredmenytalalt.append(item)
    return eredmenytalalt
    