# Sub-string divisibility
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
# order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from Problem_32 import is_pandigital

pandigital_sum = 0


def permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        r = lst[:i] + lst[i + 1:]
        for p in permutations(r):
            l.append([m] + p)
    return l


for p in permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
    if p[0] == '0':
        continue
    n = 0
    for m in p:
        n = n * 10 + int(m)
    if is_pandigital(n, 0, 9):
        if int(str(n)[1:4]) % 2 != 0:
            continue
        if int(str(n)[2:5]) % 3 != 0:
            continue
        if int(str(n)[3:6]) % 5 != 0:
            continue
        if int(str(n)[4:7]) % 7 != 0:
            continue
        if int(str(n)[5:8]) % 11 != 0:
            continue
        if int(str(n)[6:9]) % 13 != 0:
            continue
        if int(str(n)[7:]) % 17 != 0:
            continue
        pandigital_sum += n
        print(n)
print("sum:", pandigital_sum)
