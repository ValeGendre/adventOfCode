"Day 3 of Advent of code"

import string, numpy

dictionnary = string.ascii_lowercase + string.ascii_uppercase

def get_letter_score(letter:str):
    for idx, _letter in enumerate(dictionnary):
        if letter == _letter:
            return idx + 1
    raise ValueError("not a valid letter")

with open('../ressources/input.txt') as f:
    lines = [line[:-1] for line in f.readlines()]

new_line = numpy.array(lines).reshape((-1, 3))

def get_common_letter(letter_list):
    list1, list2, list3 = letter_list
    for letter in list1:
        if (letter in list2) and (letter in list3):
            return letter
    raise ValueError("not a letter in common")


print(sum(map(get_letter_score, map(get_common_letter, new_line))))