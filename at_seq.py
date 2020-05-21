#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

bases = ["A", "C", "G", "T"]
prob = [0.3, 0.2, 0.2, 0.3]
nt_count = 30

# generates a random DNA sequence as a string
seq = []
for base in range(nt_count):
    seq += random.choices(bases, weights = prob)

# calculate AT concentration
at = 0
for i in seq:
    if i == "A":   at += 1
    elif i == "T": at += 1
    else:          at += 0
at_conc = at/nt_count

print(nt_count, at_conc, "".join(seq))


"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
