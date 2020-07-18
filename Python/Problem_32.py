# Pandigital products
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


def is_pandigital(num, n_min=1, n_max=9):
    return sorted(str(num)) == [str(d) for d in range(n_min, min(10, n_max + 1))]


if __name__ == '__main__':
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    products = []
    for i in range(5000):
        for j in range(9876):
            k = i * j
            if k > 9876:
                break
            identity = [d for d in str(i)] + [d for d in str(j)] + [d for d in str(k)]
            if is_pandigital(int(''.join(identity))) and k not in products:
                products.append(k)
                print(identity, i, j, k)
    print(
        "The sum of all products whose multiplicand/multiplier/product identity can be written as 1 through 9 pandigital:",
        sum(products))
