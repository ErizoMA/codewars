def unique_in_order(iterable):
    # # Let secure that it is a string
    # iterableStr = ""
    # for i in iterable:
    #     iterableStr += str(i)
    # newList = []
    # for i in range(len(iterableStr)-1):
    #     if iterableStr[i] != iterableStr[i+1]:
    #         newList.append(iterableStr[i])
    # return newList + [iterableStr[-1]]
    d = []
    c = [x for x in iterable]
    if len(iterable) > 0:
        for i in range(len(c)-1):
            if c[i] != c[i+1]:
                d.append(c[i])
        new = d.copy()
        new.append(iterable[-1])
        return new
    else:
        return []


print(unique_in_order('ABBCcAD'))
