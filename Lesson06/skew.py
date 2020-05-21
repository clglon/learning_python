#!/usr/bin/env python3

import gzip
import sys
import biotools as bt
import argparse

# Use argparse
# Compute gc and gc-skew


"""
python3 skew.py --file genome.fa.gz --win 100 | head
I	0	0.510	-0.333
I	1	0.500	-0.360
I	2	0.490	-0.347
I	3	0.490	-0.306
I	4	0.500	-0.320
I	5	0.510	-0.333
I	6	0.510	-0.333
I	7	0.500	-0.360
I	8	0.490	-0.347
I	9	0.490	-0.306
"""
