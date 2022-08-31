import json
from utility import printDir

result = """
###################################################################################################
###################################################################################################
"""


def example():
    myDict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    print(f"myDict = {myDict}")
    print("\nfor key, value in myDict.items():")
    for key, value in myDict.items():
        print(f"    key = {key}, value = {value}")

    print(f"\nmyDict[\"one\"] = ", myDict["one"])

    print(f"\nmyDict.keys = {myDict.keys()}")
    print(f"list(myDict.keys()) = {list(myDict.keys())}")

    print("\n# Convert dict to json")
    print(f"json.dumps(myDict) = {json.dumps(myDict)}")

    print("\n# dict functions")
    printDir(dict)


example()
