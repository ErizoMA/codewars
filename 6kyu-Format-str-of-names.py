def namelist(names):
    # your code here

    listValues = []

    for i in names:
        listValues += i.values()
    if len(names) > 1:
        string = ""
        for i in range(len(listValues)-1):
            string += str(listValues[i])+", "
        string2 = string[:-2]+" & "+str(listValues[-1])
        return string2
    if len(names) == 1:
        return listValues[-1]

    else:
        return ""


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
