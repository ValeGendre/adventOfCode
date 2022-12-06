"Day 3 of Advent of code"

import string

dictionnary = string.ascii_lowercase + string.ascii_uppercase


def get_letter_score(letter: str):
    for idx, _letter in enumerate(dictionnary):
        if letter == _letter:
            return idx + 1
    raise ValueError("not a valid letter")


with open("../ressources/input.txt") as f:
    lines = [
        [line[: len(line) // 2], line[len(line) // 2 : -1]] for line in f.readlines()
    ]


def get_common_letter(letter_list):
    list1, list2 = letter_list
    for letter in list1:
        if letter in list2:
            return letter
    raise ValueError("not a letter in common")


print(sum(map(get_letter_score, map(get_common_letter, lines))))
