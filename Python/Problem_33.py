# Digit cancelling fractions
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing
# two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fractions = []
numerators = []
denominators = []
for numerator in range(11, 100):
    for denominator in range(11, 100):
        n = [int(c) for c in str(numerator)]
        d = [int(c) for c in str(denominator)]
        if numerator >= denominator:
            continue
        for digit in digits:
            if digit in n and digit in d:
                n.remove(digit)
                d.remove(digit)
                n = n[0]
                d = d[0]
                if n != 0 and d != 0 and numerator / denominator == n / d and n / d not in fractions:
                    print(numerator, denominator, n, d)
                    fractions.append(n / d)
                    numerators.append(n)
                    denominators.append(d)
                break
numerator = 1
for n in numerators:
    numerator *= n
denominator = 1
for n in denominators:
    denominator *= n
print(numerator, denominator, numerator / denominator)
