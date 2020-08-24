# Prime permutations
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
#   (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
#   but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

from Problem_26 import is_prime

primes = {}
for n in range(1234, 9877):
    if is_prime(n):
        digits = ''.join(sorted(str(n)))
        if digits in primes.keys():
            primes[digits].append(n)
        else:
            primes[digits] = [n]
print(len(primes))
primes = dict(filter(lambda x: len(x[1]) > 2, primes.items()))
print(len(primes), primes)
for permutations in primes.values():
    for p1 in range(len(permutations) - 2):
        if permutations[p1] + 3330 in permutations and permutations[p1] + 6660 in permutations:
            print(str(permutations[p1]), str(permutations[p1] + 3330), str(permutations[p1] + 6660))
