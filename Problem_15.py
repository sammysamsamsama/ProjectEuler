import math


def lattice(side):
    print(int(math.factorial(2 * side) / math.factorial(side) ** 2))


lattice(2)
lattice(3)
lattice(4)
lattice(5)
lattice(20)
