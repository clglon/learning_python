#!/usr/bin/env python3

import sys
import gzip

def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

kdscale = {"I" = 4.5, "V" = 4.2, "L" = 3.8, "F" = 2.8, "C" = 2.5, "M" = 1.9,
           "A" = 1.8, "G" = -0.4, "T" = -0.7, "S" = -0.8, "W" = -0.9,
           "Y" = -1.3, "P" = -1.6, "H" = -3.2, "E" = -3.5, "Q" = -3.5,
           "D" = -3.5, "N" = -3.5, "K" = -3.9, "R" = -4.5}
isscale = {"I" = 4.5, "V" = 4.2, "L" = 3.8, "F" = 2.8, "C" = 2.5, "M" = 1.9,
           "A" = 1.8, "G" = -0.4, "T" = -0.7, "S" = -0.8, "W" = -0.9,
           "Y" = -1.3, "P" = -1.6, "H" = -3.2, "E" = -3.5, "Q" = -3.5,
           "D" = -3.5, "N" = -3.5, "K" = -3.9, "R" = -4.5}

def cal_hydro(AAstring, method):
    if method == "KD": scale = kdscale
	elif method == "IS": scale = isscale
    hydro_score = 0
    for AA in AAstring:
        hydro_score += scale[AA]
    return hydro_score
