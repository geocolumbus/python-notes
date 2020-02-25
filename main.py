# Presumes Python 3.7.6

import sys

print("\n--- [SYSTEM] ---\n")  # #######################################################################################

print(sys.version)
print("\n")
print(sys.executable)

print("\n--- [TYPES] ---\n")  # ########################################################################################

#  Text Type:	    str
#  Numeric Types:	int, float, complex
#  Sequence Types:	list, tuple, range
#  Mapping Type:	dict
#  Set Types:	    set, frozenset
#  Boolean Type:	bool
#  Binary Types:	bytes, bytearray, memoryview

myString = "George"
print("{}\t\t{}\n".format(myString, type(myString)))

myBoolean = True
print("{} {}  {}\n".format(myBoolean, not myBoolean, type(myBoolean)))

number_decimal = 100
number_binary = 0b01101110
number_octal = 0o337
number_hex = 0xFFCCCC
number_large = 2 ** 128
number_scientific = 3.14152 ** 256
number_complex = complex(3, 5)

print("{:04d}\t\t{}\n{:#b}\t{}\n{:#o}\t\t{}\n{:#x}\t{}\n{:,d}\t{}\n{:e}\t{}\n{:.0f}\t\t{}"
      .format(number_decimal, type(number_decimal),
              number_binary, type(number_binary),
              number_octal, type(number_octal),
              number_hex, type(number_hex),
              number_large, type(number_large),
              number_scientific, type(number_scientific),
              number_complex, type(number_complex))
      )

list = ["a", "b", "c"]
print("\n{}\t\t\t\t\t\t\t{}".format(list, type(list)))

tuple = (1, 2, 3)
print("{}\t\t\t\t\t\t\t\t{}".format(tuple, type(tuple)))

myRange = range(0, 5)
print("{}\t\t\t\t\t\t\t\t{}".format(myRange, type(myRange)))

myDict = {"name": "George", "location": "Ohio"}
print("{}\t{}".format(myDict, type(myDict)))

mySet = {"one", "2", "thr33"}
print("{}\t\t\t\t\t{}".format(mySet, type(mySet)))

myFrozenSet = frozenset(mySet)
print("{}\t\t{}".format(myFrozenSet, type(myFrozenSet)))

print("\n--- [LOOPS] ---\n")  # ########################################################################################

s = ""
for x in range(0, 5):
    s += "{:d}, ".format(x)
print(s[0:-2])

print("\n--- [END] ---\n")  # ##########################################################################################
