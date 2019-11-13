import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


# 10^k = 1 (mod n) where k is the length of the period
# a = b (mod n) means that (a - b) % n == 0
# any multiples of 3 have 1 digit periods
# all numbers that can be written (2^a)(5^b) have finite decimal expansions
# all numbers that have factors co-prime to 10 and that are divisible by 2 or 5 have some initial non-period
# only looking at primes will suffice
# all other numbers have similar periods after some initial non-period
def repeating_cycle(n):
    if n % 3 == 0:
        return 1
    if n % 2 == 0 or n % 5 == 0:
        return 0
    for k in range(1, 1000):
        if (10 ** k - 1) % n == 0:
            return k
    return 0


if __name__ == '__main__':

    longest_period_num = 1
    longest_period = 1
    for d in range(1, 1000):
        if not is_prime(d):
            continue
        period = repeating_cycle(d)
        if period > longest_period:
            longest_period_num = d
            longest_period = period
        print(d, period, 1 / d)
    print("longest_period_num : " + str(longest_period_num))
    print("longest_period : " + str(longest_period))
