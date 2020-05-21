#!/usr/bin/env python3

# Write a program that compares two files of names to find:
#	Names unique to file 1
#	Names unique to file 2
#	Names shared in both files

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

def mkdict(filename):
    dictionary = {}
    with open(filename) as fp:
        for word in fp.readlines():
            word = word.rstrip()
            dictionary[word] = True
    return dictionary

d1 = mkdict(file1)
d2 = mkdict(file2)
print(d1, d2)

u1 = []
u2 = []
both = []

for word in d1:
    if word in d2: both.append(word)
    else:          u1.append(word)

for word in d2:
    if word in d1: u2.append(word)

print(u1, u2, both)

"""
python3 checklist.py --file1 --file2
"""
