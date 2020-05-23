#!/usr/bin/env python3

import gzip
import sys
import argparse
import biotools

# Write a program that finds peptidies within protein sequences
# Command line:
#	python3 pepsearch.py IAN


parser = argparse.ArgumentParser(
	description='Search for peptides in proteins.')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='fasta file')
parser.add_argument('--pattern', required=True, type=str,
	metavar='<str>', help='peptide pattern')
arg = parser.parse_args()

for name, seq in biotools.read_fasta(arg.file):
	if arg.pattern in seq: print(name, len(seq))


"""
python3 pepsearch.py proteins.fasta.gz IAN | wc -w
	43
"""
