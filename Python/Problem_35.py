# Circular primes
#
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from Problem_26 import is_prime


def rotations(n):
    digits = [int(d) for d in str(n)]
    permutations = []
    while digits not in permutations:
        permutations.append(digits.copy())
        digits.insert(0, digits.pop())
    return permutations


if __name__ == '__main__':
    circular_primes = []
    for n in range(2, 1000000):
        if is_prime(n):
            rots = [is_prime(int("".join([str(d) for d in rotation]))) for rotation in rotations(n)]
            if False not in rots:
                temp_list = []
                for rotation in rotations(n):
                    temp_list.append(int("".join([str(d) for d in rotation])))
                print(n, temp_list, rots)
                circular_primes.append(n)
    print(circular_primes)
    print("There are *{}* circular primes below one million.".format(len(circular_primes)))
