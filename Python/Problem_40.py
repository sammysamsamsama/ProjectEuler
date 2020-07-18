# Champernowne's constant
#
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.12345678910*1*112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If d_n represents the nth digit of the fractional part, find the value of the following expression.
#
# d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

d = ''
n = 1
while len(d) < 1000000:
    d += str(n)
    n += 1

print("d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000 =",
      int(d[0]) * int(d[9]) * int(d[99]) * int(d[999]) * int(d[9999]) * int(d[99999]) * int(d[999999]))
