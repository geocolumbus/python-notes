import json
from utility import printDir

result = """
####################################################################################################
myList = [1, 2, 3, 4, 5]
myList = list((1, 2, 3, 4, 5))
type(myList) == list  =>  True
len(myList) = 5

myList[0:] = myList[:] = ['george', 'kelly', 'alex', 'zach', 'anne']
myList[0:0] = []
myList[0:2] = myList[:2] = ['george', 'kelly']
myList[2:5] = ['alex', 'zach', 'anne']
myList[3] = zach

myList[-1:] = anne
myList[-3:] = ['alex', 'zach', 'anne']
myList[-3:-1] = ['alex', 'zach']

for i in myList:
i = george
i = kelly
i = alex
i = zach
i = anne

for i, j in enumerate(myList):
i = 0, j = george
i = 1, j = kelly
i = 2, j = alex
i = 3, j = zach
i = 4, j = anne

myList2 = myList     # Assign same data to two names
myList2 = myList[:]  # Make a copy of a list

# Convert list to string
", ".join(myList) = "george, kelly, alex, zach, anne"

# Convert string to list
myStr.split(", ") = ['one', 'two', 'three', 'four', 'five']

# Convert range to list
list(range(1, 6)) = [1, 2, 3, 4, 5]

# Convert list to json
json.dumps(myList) = ["george", "kelly", "alex", "zach", "anne"]

# list functions
append                        clear                         copy
count                         extend                        index
insert                        pop                           remove
####################################################################################################
"""


def example():
    myList = ["george", "kelly", "alex", "zach", "anne"]
    # myList = list((1, 2, 3, 4, 5))
    print(f"myList = [1, 2, 3, 4, 5]\nmyList = list((1, 2, 3, 4, 5))")
    print(f"type(myList) == list  =>  {type(myList) == list}")
    print(f"len(myList) = {len(myList)}")
    print()
    print(f"myList[0:] = myList[:] = {myList[0:]}")
    print(f"myList[0:0] = {myList[0:0]}")
    print(f"myList[0:2] = myList[:2] = {myList[0:2]}")
    print(f"myList[2:5] = {myList[2:5]}")
    print(f"myList[3] = {myList[3]}")
    print()
    print(f"myList[-1:] = {myList[-1]}")
    print(f"myList[-3:] = {myList[-3:]}")
    print(f"myList[-3:-1] = {myList[-3:-1]}")
    print()

    # iterate through list
    print("for i in myList:")
    for i in myList:
        print(f"i = {i}")

    print()

    # iterate through list with index
    print("for i, j in enumerate(myList):")
    for i, j in enumerate(myList):
        print(f"i = {i}, j = {j}")

    print()

    print("myList2 = myList     # Assign same data to two names")
    print("myList2 = myList[:]  # Make a copy of a list")

    print("\n# Convert list to string")
    print(f"\", \".join(myList) = \"{', '.join(myList)}\"")

    print("\n# Convert string to list")
    myStr = "one, two, three, four, five"
    print(f"myStr.split(\", \") = {myStr.split(', ')}")

    print("\n# Convert range to list")
    print(f"list(range(1, 6)) = {list(range(1, 6))}")

    print("\n# Convert list to json")
    print(f"json.dumps(myList) = {json.dumps(myList)}")

    print("\n# list functions")
    printDir(list)


example()
