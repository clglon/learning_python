#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# Use fileinput to get the data from nucleotides.txt
# Make sure that the values are probabilities
# Make sure that the distribution sums to 1
# Report with 3 decimal figures

import fileinput
import math

# using a dictionary makes more sense to me
data = {}
for line in fileinput.input():
    #if line[0] == '#': continue # skip over comments
    if line.startswith('#'): continue # same as above
    line = line.rstrip() # remove newline (return character), often useful
    data[line[0]] = float(line[2:])
# print(data)
# {'A': '0.1', 'C': '0.2', 'G': '0.3', 'T': '0.4'}

# file check for
# each value is a probabilities
# the sum of values is equal to one

bases = 0
for prob in data:
    dist_sum = 0
    for value in data:
        if data[value] <= 1:
            dist_sum += data[value]
        else:
            print("Nucleotide Probability of", value, "is", data[value])
            continue
    if dist_sum == 1:
        shannon = data[prob] * math.log2(data[prob])
        bases += shannon
    else:
        print("Distribution Sum does not equal 1")
        break
bases = bases * -1
print(f'{(bases):.3f}')

# what if one of the probabilities was zero?

"""
python3 entropy.py nucleotides.txt
1.846
"""
