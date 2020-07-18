# Coin sums
#
# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

coins = [2, 5, 10, 20, 50, 100, 200]
# amounts to make change with from [0, 200]
change = list(range(201))
# number of ways to make change for index
ways_to_make_change = [1] * 201

for coin in coins:
    for change in range(201):
        # don't check how many ways to make 1p with a 2p coin, etc.
        if change >= coin:
            # remove coin from value, then find number of ways to make change from new value
            # 5p - 2p = 3p is one new solution, so add it * how many ways you can make 3p
            new_change = change - coin
            ways_to_make_change[change] += ways_to_make_change[new_change]
    print(coin, list(zip(range(201), ways_to_make_change)))
print("Numbers of ways to make £2 from any number of coins:", ways_to_make_change[-1])
