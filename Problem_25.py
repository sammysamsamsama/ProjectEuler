fibs = [1, 1]
index = 2

while len(str(fibs[1])) < 1000:
    fibs.append(fibs[0] + fibs[1])
    del fibs[0]
    index += 1
    # print(index, fibs[1])

print(index, fibs[1])
