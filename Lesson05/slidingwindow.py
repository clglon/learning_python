#!/usr/bin/env python3


# use sliding window to calculate AT concentration

seq = "ACGTATCGTCGTAGCTCGTCTCGATGCTAGCCTAGCTAGC"
prob = { "A":0.3, "C":0.2, "G":0.2, "T":0.3 }
window = 8

at_conc = 0
for nt in seq:
    if nt in prob: at_conc += prob[nt]
    else: print("else")
print(at_conc/len(seq))
