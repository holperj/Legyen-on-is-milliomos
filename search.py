def search_by_name(results, name):
    for index, item in enumerate(results):
        if item.name == name:
            return index
    return False

def search_by_name2(results, name):
    for item in results:
        if item.name == name:
            return item
    return False
    
def search_under(results, limit):
    failed_students = []
    for item in results:
        if item.result < limit:
            failed_students.append(item)
    return failed_students