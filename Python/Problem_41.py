# Pandigital prime
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

from Problem_26 import is_prime
from Problem_32 import is_pandigital

largest_n_digit_pandigital_prime = 1
# start from 7654321 because {987654321} (9-digit pandigitals) and {87654321} are divisible by 3 and so not prime
# remember that if the sum of a number's digits is divisible by 3, the number is also divisible by 3
n = 7654321
while largest_n_digit_pandigital_prime == 1:
    if is_prime(n) and is_pandigital(n, len(str(n))):
        print(n, "is prime and is a {}-digit pandigital".format(len(str(n))))
        largest_n_digit_pandigital_prime = n
        break
    n -= 2
print(largest_n_digit_pandigital_prime)
