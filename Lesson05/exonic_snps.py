#!/usr/bin/env python3

# Write a program that intersects SNPs and coding exons
# snps.txt.gz has all the 23andme snps on chrom 21
# exons.txt.gz has all the coding exons on chrom 21
# Report:
#	number of SNPs
#	number of genes
#	number of exons
#	names of genes with SNPs in them
# Given that there are about 100x more genes in the human genome
#	And 100x more SNPs on the full chip
#	Estimate how long your program would take to run using all available data


"""
SNPs: 8607
Genes: 234
Exons: 2433
Genes w/ SNPs: 54
Gene List: ABCG1, AGPAT3, AIRE, AP000311.1, BACE2, BACH1, BRWD1, C21orf58, C2CD2, CBS, CHAF1B, CLDN17, COL6A1, COL6A2, DNMT3L, DOP1B, DSCAM, FAM243A, GART, IFNAR1, IFNGR2, ITGB2, KRTAP10-5, KRTAP10-7, KRTAP19-3, KRTAP25-1, MCM3AP, MORC3, PAXBP1, PCNT, PDE9A, PDXK, PIGP, PRDM15, PTTG1IP, PWP2, RRP1, RWDD2B, SCAF4, SIK1, SIM2, SLC37A1, SLC5A3, SOD1, SON, SYNJ1, TMPRSS15, TMPRSS2, TMPRSS3, TRAPPC10, TTC3, U2AF1, UMODL1, USP25
Estimated Full Time: 4.76 hours
"""
