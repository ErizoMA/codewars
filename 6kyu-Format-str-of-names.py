def namelist(names):
    # your code here
    if len(names) > 0:

        listValues = []

        for i in names:
            listValues += i.values()

        strListValues = " & ".join(listValues)

        return strListValues.replace("&", ",", len(listValues)-2)
    else:
        return ""


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
