#!/usr/bin/env python3

import gzip
import sys

# Write a program that finds all of the open reading frames in a transcript
# ORFs start with ATG and end with a stop codon (TAA, TAG, TGA)
# See below for command line and expected output


"""
python3 longest_orf.py transcripts.fasta.gz  | head
CBG00001.1 720 525
CBG00006.1 1310 870
CBG00032.1 1985 1737
CBG00035.1 1867 1716
CBG00041.1 1075 891
CBG00049.1 693 189
CBG00050.1 1797 1245
CBG00056.1 1545 1392
CBG00059.1 1567 1488
CBG00060.1 1488 1296

python3 fasta_stats.py transcripts.fasta.gz fasta_stats.py -
Count: 232
Total: 278793
Min: 603
Max: 1991
Mean: 1201.7
NTs: 0.291 0.218 0.210 0.281

python3 rand_fasta.py 232 603 1991 0.291 0.218 0.210 0.281 | python3 fasta_stats.py -
Count: 232
Total: 311538
Min: 605
Max: 1990
Mean: 1342.8
NTs: 0.291 0.219 0.210 0.280

python3 rand_fasta.py 232 603 1991 0.291 0.218 0.210 0.281 | python3 longest_orf.py - | head
seq-0 1833 165
seq-1 1759 387
seq-2 1677 81
seq-3 1765 144
seq-4 1347 135
seq-5 1141 180
seq-6 1127 240
seq-7 1532 162
seq-8 1376 78
seq-9 793 213
"""
