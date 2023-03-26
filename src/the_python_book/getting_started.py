#!/user/bin/env python3

import sys

target_int = input("How many integers?")

try:
    target_int = int(target_int)
except ValueError:
    sys.exit("Please enter an integer")

ints = list()

count = 0

while count < target_int:
    new_int = input(f"Please enter integer {count + 1}:"4)
    isint = False
    try:
        new_int = int(new_int)
        isint = True
    except ValueError:
        print("You must enter an integer")

    if isint == True:
        ints.append(new_int)
        count += 1

print("Using a for loop")
for value in ints:
    print(str(value))

# Or with a while loop:
print("Using a while loop")
total = len(ints)
count = 0
while count < total:
    print(str(ints[count]))
    count += 1
