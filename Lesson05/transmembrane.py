#!/usr/bin/env python3

import gzip
import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

'''
plan:
> import biotools for read_fasta function
> create dictionary with KD scale
> create sliding window function ?
> check the first 30 aa for:
    signal peptide window length = 8
    with a KD > 2.5
> check all aa after the first 30 aa for:
    Hydrophobic region window length = 11
    with a KD > 2.0
> print out list of aa name that is a transmembrane protein
'''

# import read_fasta function to read fasta file
from biotools import read_fasta

# create dictionary with KD scale
def read_scale(filename):
    scaledict = {}
    with open(filename, "r") as f:
        for line in f:
            aa = line.split()
            if len(aa) == 2:
                key, values = aa[0], float(aa[1])
                scaledict[key] = values
    return scaledict

kd = read_scale("kdscale.txt")
print(kd)

def transmembrane(seq, w, t):
    for i in range(len(seq) - w + 1):
        win = seq[i:i + w]
        h = 0
        for aa in win:
            if aa in kd:
                h += kd[aa]
        have = h/w
        if have >= t:
            return True
    return False


for name, protein in read_fasta(sys.argv[1]):
    nterm = protein[:30]
    cterm = protein[30:]
    if transmembrane(nterm, 8, 2.5) and transmembrane(cterm, 11, 2.0):
        print(name)






"""
python3 transmembrane.py proteins.fasta.gz
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
