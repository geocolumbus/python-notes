#  [!s | !r | !a][[fill]align][sign][#][0][minimumwidth][.precision][type]

#  !s       Calls str()
#  !r       Calls repr()  -> printable representation
#  !a       Calls ascii() -> escapes the non-ASCII characters in the string using \x, \u or \U

#  fill    Any character to fill any extra space (precedes the alignment character)
#  <       left-aligned (default for objects)
#  >       right-aligned (default for numbers)
#  ^       centered
#  =       fill space between sign and number

#  +       both positive and negative sign are shown
#  -       only negative sign is shown
#  " "     space for positive, "-" for negative

#  #       Alternate form (*before width)
#  ,       Adds "," as thousands separator
#  _       Adds "_" as thousands separator

#  f / F   Floating point
#  d       Integer (decimal - default for int)
#  %       Percentage
#  b       Binary
#  o       Octal
#  x / X   Hex
#  e / E   Exponential
#  g / G   General (default for float)
#  n       number (generic)
#  c       character (unicode)

result = """
####################################################################################################
<class 'str'>         123
<class 'int'>         123
<class 'float'>       123.0
<class 'complex'>     (123+0j)
<class 'list'>        [1, 2, 3]
<class 'tuple'>       (1, 2, 3)
<class 'range'>       range(0, 3)
<class 'dict'>        {'name': 'george', 'age': 55}
<class 'set'>         {1, 2, 3}
<class 'frozenset'>   frozenset({1, 2, 3})
<class 'bool'>        True
<class 'bool'>        False
<class 'bytes'>       b'George'
<class 'bytearray'>   bytearray(b'George')
<class 'memoryview'>  <memory at 0x102615f40>
####################################################################################################
"""


def example():
    p = []

    p.append(str(123))  # string

    p.append(int(123))  # integer
    p.append(float(123))  # float
    p.append(complex(123))  # complex

    p.append([1, 2, 3])  # list
    p.append((1, 2, 3))  # tuple
    p.append(range(3))  # range
    p.append({"name": "george", "age": 55})  # dict
    p.append({1, 2, 3})  # set
    p.append(frozenset({1, 2, 3}))  # frozen set

    p.append(True)
    p.append(False)

    p.append(bytes("George", "utf-8"))
    p.append(bytearray("George", "utf-8"))
    p.append(memoryview(bytes([1, 2, 3])))

    for item in p:
        print(
            f"{type(item)!s:21} {item}")  # 3.6 or greater  # print("{0!s:21} {1}".format(type(
        # item), item))   # < 3.6  # print("%21s %s" % (str(type(item)), str(item)))  # 2


example()
