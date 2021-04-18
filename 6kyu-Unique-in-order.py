def unique_in_order(iterable):
    newList = []
    for i in iterable:
        if len(newList) == 0 or i != newList[-1:]:
            newList.append(i)
    return newList


print(unique_in_order('ABBCcAD'))
