# Pandigital multiples
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
# with (1,2, ... , n) where n > 1?

from Problem_32 import is_pandigital

largest_pandigital = 1
for n in range(1, 9999):
    products = []
    i = 1
    while len(''.join(products)) < 9:
        products.append(str(n * i))
        i += 1
    concatenated_product = int(''.join(products))
    if is_pandigital(concatenated_product) and concatenated_product > largest_pandigital:
        largest_pandigital = concatenated_product
print("Largest 1 to 9 pandigital formed as the concatenated product of an integer with (1,2,...,n) where n > 1:",
      largest_pandigital)
