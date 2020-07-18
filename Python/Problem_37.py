# Trunctable primes
#
# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from Problem_26 import is_prime


def is_trunctable_prime(n):
    if not is_prime(n):
        return False
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[i:])) or not is_prime(int(n[:-i])):
            return False
    return True


if __name__ == '__main__':
    trunctable_primes = []
    n = 23
    while len(trunctable_primes) < 11:
        if is_trunctable_prime(n):
            trunctable_primes.append(n)
        n += 2
    print("The sum of the only eleven primes that are both trunctable from left to right and right to left:",
          sum(trunctable_primes))
    print("The eleven primes:", trunctable_primes)
