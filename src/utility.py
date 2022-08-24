def removePrivateMembers(myList):
    return [x for x in myList if not x.startswith("_")]

def printThreeColumns(myList):
    for a, b, c in zip(myList[::3], myList[1::3], myList[2::3]):
        print('{:<30}{:<30}{:<}'.format(a, b, c))
    return

def printFiveColumns(myList):
    for a, b, c, d, e in zip(myList[::5], myList[1::5], myList[2::5], myList[3::5], myList[4::5]):
        print('{:<30}{:<30}{:<30}{:<30}{:<}'.format(a, b, c, d, e))
    return


def printDir(item):
    printThreeColumns(removePrivateMembers(dir(item)))
    return
