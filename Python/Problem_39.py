# Integer right triangles
#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

import math

p_max_solutions = 1
max_solutions = 1
for p in range(12, 1000):
    solutions = []
    for i in range(1, p // 2):
        for j in range(i, p - i):
            k = math.sqrt(i ** 2 + j ** 2)
            if int(k) == k and k + i + j == p:
                # print(p, i, j, int(k))
                solutions.append({i, j, int(k)})
    num_solutions = len(solutions)
    if num_solutions > max_solutions:
        print(p, num_solutions, solutions)
        p_max_solutions = p
        max_solutions = num_solutions
print("Value of p <= 1000 with max solutions:", p_max_solutions)
