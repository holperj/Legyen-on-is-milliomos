import random
from adatok import result

def loadData():
    results = []
    
    file = open("IKTkerdesek.csv","r",encoding="utf-8")
    
    
    for row in file:
        splitted = row.split(";")
        res = result()
        res.kerdes = splitted[0]
        res.valasz1 = splitted[1]
        res.valasz2 = splitted[2]
        res.valasz3 = splitted[3]
        res.valasz4 = splitted[4]
        
       

        results.append(res)

    file.close()

    return results
