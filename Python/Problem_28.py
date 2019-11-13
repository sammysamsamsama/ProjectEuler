def spiral_diagonals(n):
    a = 1
    total = 1
    counter = 2
    adds = 0
    while a < n ** 2:
        if adds < 4:
            a += counter
            total += a
            adds += 1
        else:
            counter += 2
            a += counter
            total += a
            adds = 1
    print(total)


if __name__ == "__main__":
    spiral_diagonals(1001)
