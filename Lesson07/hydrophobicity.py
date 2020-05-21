#!/usr/bin/env python3

# Write a program that computes hydrophobicity in a window
# Let the user choose the method (see below)
# https://en.wikipedia.org/wiki/Hydrophilicity_plot
# https://en.wikipedia.org/wiki/Hydrophobicity_scales

import sys
import biotools as scale

parer = argparse.ArgumentParser(
    description='hydrophobicity calculator')
parser.add_argument('--window', required=False, type=int, default=15,
	metavar='<int>', help='Window Size, default [%(default)i]')
parser.add_argument('--method', required=False, type=str, default='KD',
	metavar='<str>', help='Calculation Method, KD, IS, OS, IS+OS, CC, default [%(default)i]')
arg = parser.parse_args()

print(scale.cal_hydro("CELINE", "KD"))

"""
python3 hydrophobicity.py --input proteins.fasta.gz --window 11 --method kd
"""

# add this code to biotools? how to import biotools
