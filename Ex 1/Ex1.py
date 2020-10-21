# Ex1 - Monday Oct 19, 2020
# Name: Sagie Baram, ID: 205591829
# Name: Eden Mozes, ID: 315997049

import sys

# sys contains low level information about the precision
# and internal representation.


def func(a, b, c, d, e):
    """
    Func recieves 5 parameters a, b, c, d, e and computes them.

    @return an absolute value of the computation formula.
    """
    return abs(a * (b / c - d) - e)


def __main__():
    """
    Substracts from the returned value by an epsilon.

    *epslion* : difference between 1.0 and the least value greater than 1.0
    that is representable as a float.

    """
    # We will insert values to variables, assuming they are numbers.
    var1 = float(input("Enter var 1: "))
    var2 = float(input("Enter var 2: "))
    var3 = float(input("Enter var 3: "))
    var4 = float(input("Enter var 4: "))
    var5 = float(input("Enter var 5: "))

    result = func(var1, var2, var3, var4, var5) - sys.float_info.epsilon
    print("The result is: ", result)


__main__()
