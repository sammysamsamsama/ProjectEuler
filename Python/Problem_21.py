# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math


def d(div):
    if div == 0:
        return 0
    if div == 1:
        return 1

    divisors = 1

    for i in range(2, int(math.sqrt(div)) + 1):
        if div % i == 0 and i ** 2 != div:
            divisors += i
            divisors += div // i
    if int(math.sqrt(div)) ** 2 == div:
        divisors += int(math.sqrt(div))
    return divisors


if __name__ == '__main__':
    sum = 0
    amicable_nums = []

    for a in range(1, 10000):
        b = d(a)
        if a == d(b) and not amicable_nums.__contains__(a) and a != b:
            sum += a + b
            amicable_nums.append(a)
            amicable_nums.append(b)
    print(sum)
