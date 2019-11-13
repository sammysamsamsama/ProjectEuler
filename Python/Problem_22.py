alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('E:\IdeaProjects\ProjectEulerPython\p022_names.txt') as names_list:
    names = names_list.read().strip('"').split('","')
    names = sorted(names)
    s = 0
    for name in names:
        score = 0
        index = names.index(name) + 1
        for letter in list(name):
            score += alpha.find(letter) + 1
        score *= index
        s += score
    print(s)
