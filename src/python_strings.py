from utility import printDir

result = """
# str functions
capitalize                    casefold                      center
count                         encode                        endswith
expandtabs                    find                          format
format_map                    index                         isalnum
isalpha                       isascii                       isdecimal
isdigit                       isidentifier                  islower
isnumeric                     isprintable                   isspace
istitle                       isupper                       join
ljust                         lower                         lstrip
maketrans                     partition                     removeprefix
removesuffix                  replace                       rfind
rindex                        rjust                         rpartition
rsplit                        rstrip                        split
splitlines                    startswith                    strip
swapcase                      title                         translate
"""


def example():
    print("\n# str functions")
    printDir(str)
    return


example()
