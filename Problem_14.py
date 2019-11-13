# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

def collatz(x):
    num_with_longest_chain = 1
    longest_chain = 1
    for num in range(1, x):
        chain = 1
        n = num
        while n != 1:
            if n % 2 == 0:
                n /= 2
                chain += 1
            else:
                n = (3 * n + 1) / 2
                chain += 2
        if chain > longest_chain:
            longest_chain = chain
            num_with_longest_chain = num
        # print(num, chain)
    print(num_with_longest_chain, longest_chain)


collatz(1000000)
