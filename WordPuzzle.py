import itertools


def get_value(letters, word):
    value = 0
    word_length = len(word)
    for i in range(0, word_length):
        letter = word[i]
        value += letters.index(letter) * pow(10, word_length - i - 1)
    return value


def solve_puzzle(terms, result):
    base = set()
    for word in terms:
        for letter in word:
            base.add(letter)

    for letter in result:
        base.add(letter);

    base = list(base)
    base_len = len(base)
    for i in range(0, 10 - base_len):
        base.append(i)

    print(base)

    for a in itertools.permutations(base):
        terms_values = []
        for term in terms:
            terms_values.append(get_value(a, term))

        if sum(terms_values) == get_value(a, result):
            # print(a)
            print(terms_values, get_value(a, result))

    print('  -- END --  ')


# solve_puzzle(['SEND', 'MORE'], 'MONEY')
# solve_puzzle(['SINUS', 'SINUS', 'KOSINUS'], 'TANGENS')
# solve_puzzle(['ABD', 'DEF'], 'GHIJ')
solve_puzzle(['SIX', 'SEVEN', 'SEVEN'], 'TWENTY')
