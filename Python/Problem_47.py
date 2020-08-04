# Distinct primes factors
#
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
# 
# answer: 134043

from Problem_26 import is_prime


def prime_factors(n):
    if is_prime(n):
        return [n]
    factors = []
    for num in range(2, n // 2 + 1):
        if is_prime(num):
            if n % num == 0:
                factors.append(num)
                while n % num == 0:
                    n //= num
                if n == 1:
                    break
                continue
    return factors


if __name__ == '__main__':
    n = 130000
    nums = []
    while True:
        if len(prime_factors(n)) == 4:
            nums.append(n)
            if len(nums) > 1:
                if len(nums) == 2:
                    print(n - 1, prime_factors(n - 1))
                print(n, prime_factors(n))
            if len(nums) == 4:
                break
        else:
            if len(nums) > 0:
                if len(nums) > 1:
                    print("----------")
                nums.clear()
        n += 1
