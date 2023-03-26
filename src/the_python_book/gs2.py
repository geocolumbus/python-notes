#!/usr/bin/env python3


def test(passedlist, name):
    name = "Fred"
    count = 0
    for key, value in enumerate(mylist):
        mylist[key] = count
        count -= 1


name = "George"
mylist = list(range(1, 6))
print(name, mylist)
test(mylist, name)
print(name, mylist)
