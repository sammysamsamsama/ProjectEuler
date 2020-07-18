# Digit factorials
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
f = [1, 1, 2]


def factorial(n):
    if n <= len(f) - 1:
        return f[n]
    else:
        f.append(n * factorial(n - 1))
        return f[n]


if __name__ == '__main__':
    digit_factorials = []
    for n in range(3, 99999):
        digits = [int(d) for d in str(n)]
        factorials = [factorial(d) for d in digits]
        if sum(factorials) == n:
            print(n, digits, factorials)
            digit_factorials.append(n)
    print("The sum of all numbers equal to the sum of the factorial of their digits:", sum(digit_factorials))
