# Self powers
#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

if __name__ == '__main__':
    series = []
    for i in range(1, 1001):
        series.append(i ** i)
    # print(series)
    print(str(sum(series))[-10:])
