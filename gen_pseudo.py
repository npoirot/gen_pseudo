#!/usr/bin/env python

import random
random.seed()

nb_pseudos = 10

range_min = 1
range_max = 26
offset = ord('a')

len_min = 5
len_max = 9

vowels = "aeiouy"
max_cvowels = 2
max_ccons = 3

def getRandomName(l):
    pseudo = ""
    count_v = 0
    count_c = 0
    for i in range(1, l + 1):
        letter = getRandomChar(i)
        if letter in vowels:
            count_c = 0
            count_v += 1
        else:
            count_c += 1
            count_v = 0
        if count_c > max_cvowels or count_v > max_ccons:
            return False
        else:
            pseudo += letter
    return pseudo

def getRandomChar(x):
    return chr(random.randint(range_min - 1, range_max - 1) + offset)

def gen_1_pseudo():
    length = random.randint(len_min, len_max)
    res = getRandomName(length)
    while res == False:
        res = getRandomName(length)
    return res.capitalize()

for i in range(1, nb_pseudos + 1):
    print(gen_1_pseudo())
