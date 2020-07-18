# Double-base palindromes
#
# The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def decimal_to_binary(n):
    if n == 0:
        return 0
    binary = []
    while n > 0:
        binary.insert(0, '0' if n % 2 == 0 else '1')
        n //= 2
    binary = int(''.join(binary))
    return binary


def palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    sum = 0
    for n in range(1000000):
        if palindrome(n) and palindrome(decimal_to_binary(n)):
            sum += n
    print("The sum of all numbers < 1M which are palindromic in base 10 and base 2:", sum)
