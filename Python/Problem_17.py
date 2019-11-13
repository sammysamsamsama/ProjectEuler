words = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eighty', 90: 'ninety'}


def num_to_word(num):
    if num <= 19:
        # print(words.get(num), len(str(words.get(num))))
        return words.get(num)
    # first 10s
    word = ''
    if num <= 99:
        word += words.get(num // 10 * 10)
        word += str(words.get(num % 10))
        # print(word, len(str(word)))
        return str(word)
    elif num <= 999:
        word += str(words.get(num // 100) + 'hundred')
        if num % 100 != 0:
            word += 'and' + str(num_to_word(num % 100))
        # print(word, len(str(word)))
        return str(word)
    elif num <= 9999:
        word += words.get(num // 1000) + 'thousand'
        word += num_to_word(num % 1000)
        # print(word, len(str(word)))
        return str(word)
    else:
        return 'greater than 9999'


ans = 0
for n in range(1, 1001):
    ans += len(num_to_word(n))
    # print(num_to_word(n), len(num_to_word(n)))
print(ans)
