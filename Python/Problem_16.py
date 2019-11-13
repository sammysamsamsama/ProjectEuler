def power_sum(x):
    num = 2 ** x
    sum = 0
    while int(num) > 0:
        print(sum, num)
        sum += num % 10
        num //= 10
    print(sum)


power_sum(1000)
