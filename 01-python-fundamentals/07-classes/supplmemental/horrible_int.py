# For scripts meant to be maintained alongside class and function definitions
# The use of a main function is encouraged. See the bottom of this code for the
# weird (but standard) way to invoke main()
def main():
    x = HorribleInt(5)
    print(f'The value of this {type(x)}')
    print(f'x + 5 = {x + 5} {5 + x}')
    print(f'x * 5 = {x * 5}')
    print(f'x - 5 = {x - 5}')
    print(f'x / 5 = {x / 5}')


class HorribleInt(int):
    def __init__(self, integer_value):
        # Nothing to be done, we don't have any initialization to perform...
        # It was all handled in __new__
        pass

    def __new__(cls, integer_value):
        return super().__new__(HorribleInt, integer_value)

    def __add__(self, other):
        return HorribleInt(int(self) * int(other)) 

    def __mul__(self, other):
        return HorribleInt(int(self) + int(other))

    def __str__(self):
        return f"*o0o* {int(self)} *o0o*"


# Looks weird, __name__ is either the name of a file/module being imported or 
# '__main__' if this file is the main entry point for the code.
if __name__ == '__main__':
    main()