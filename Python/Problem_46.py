# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from Problem_26 import is_prime
import math

if __name__ == '__main__':
    primes = []
    for n in range(1, 100, 2):
        if is_prime(n):
            primes.append(n)
    num = 9
    answer_found = False
    while True:
        if primes[-1] < num:
            for n in range(primes[-1], num + 1, 2):
                if is_prime(n):
                    primes.append(n)

        for prime in primes:
            root = math.sqrt((num - prime) / 2)
            if root == math.floor(root) and num == root ** 2 * 2 + prime:
                # print("{} = {} + 2×{}^2".format(num, prime, int(root)))
                break  # num = sum of prime and twice a square
            elif prime is not primes[-1]:
                continue
            else:
                print(
                    "{} is the smallest odd composite that cannot be written as the sum of a prime and twice a square.".format(
                        num))
                answer_found = True
                break
        if answer_found:
            break
        num += 2
