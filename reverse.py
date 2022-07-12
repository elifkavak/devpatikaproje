first = [[1, 2], [3, 4], [5, 6, 7]]
newlist = []
def flatten(flatList):
    first.reverse()
    for i in flatList:
        if isinstance(i, list):
            i.reverse()
            newlist.append(i)
        else:
            newlist.append(i)
    return newlist

print(flatten(first))