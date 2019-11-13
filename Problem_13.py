with open("E:\IdeaProjects\ProjectEulerPython\Problem_13") as problem_13:
    sum = 0
    for line in problem_13:
        sum += int(line)
    sum_str = str(sum)
    print("first_10_sum: " + sum_str[0:10])
