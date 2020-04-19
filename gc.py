#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gc = 0

for i in range(0, len(dna)):
    if dna[i] == 'G' or dna[i] == 'C': gc += 1
    else: gc += 0

gc_percent = gc / len(dna)

# formating options
print(round(gc_percent, 2))
print('%.2f' % gc_percent)
print('{:.2f}'.format(gc_percent))
print(f'{gc_percent:.2f}')
# print(f'{gc_percent}) I dont know

"""
0.42
0.42
0.42
"""
