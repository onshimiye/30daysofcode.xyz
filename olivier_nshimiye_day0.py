def i(char):
    # return index of a character in an array of 26 items
    return ord(char) - 65


def scrabble_score(word):
    char_score = [1 for c in range(26)]

    char_score[i('D')] = char_score[i('G')] = 2
    char_score[i('B')] = char_score[i('C')] = char_score[i('M')] = char_score[i('P')] = 3
    char_score[i('F')] = char_score[i('H')] = char_score[i('V')] = char_score[i('W')] = char_score[i('Y')] = 4
    char_score[i('K')] = 5
    char_score[i('J')] = char_score[i('X')] = 8
    char_score[i('Q')] = char_score[i('Z')] = 10

    score = 0

    for c in word:
        score += char_score[ord(c.upper()) - 65]

    return score

