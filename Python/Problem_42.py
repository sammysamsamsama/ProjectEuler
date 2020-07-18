# Coded triangle numbers
#
# The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical
# position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words, how many are triangle words?


def triangle_number(n):
    return int(n / 2 * (n + 1))


words_txt = open('C:\\Users\\sammy\\Desktop\\All\\ProjectEuler\\Python\\p042_words.txt')
words = [w.strip('"') for w in words_txt.read().split(',')]
alphabet = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
triangle_numbers = [triangle_number(n) for n in range(1, 10)]
num_triangle_numbers = 0
for word in words:
    word_value = sum(alphabet.index(letter) for letter in word)
    if word_value > triangle_numbers[-1]:
        while triangle_numbers[-1] < word_value:
            triangle_numbers.append(triangle_number(len(triangle_numbers) + 1))
    if word_value in triangle_numbers:
        num_triangle_numbers += 1
        print(num_triangle_numbers, word, word_value, triangle_numbers)
print(num_triangle_numbers, triangle_numbers)
