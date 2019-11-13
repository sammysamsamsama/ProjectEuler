import math

num = math.factorial(100)
print(num)

digits = [int(x) for x in str(num)]
print(digits)

sum = 0
for digit in digits:
    sum += digit

print(sum)
