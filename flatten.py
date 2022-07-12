first = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
newlist = []
def flatten(flatList):

    for i in flatList:
        if isinstance(i, list):
            flatten(i)
        else:
            newlist.append(i)
    return newlist

print(flatten(first))