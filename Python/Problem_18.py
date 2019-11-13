with open('E:\IdeaProjects\ProjectEulerPython\Problem_18') as pyramid:
    array = []
    num_lines = 0
    for line in pyramid:
        num_lines += 1
        array.append([int(x) for x in line.split(" ")])
    # print(array)
    for l in range(num_lines - 2, -1, -1):
        for i in range(0, len(array[l])):
            b = array[l + 1][i]
            c = array[l + 1][i + 1]
            array[l][i] = array[l][i] + max(b, c)
        del array[l + 1]
        # print(array)
    print(array[0][0])
