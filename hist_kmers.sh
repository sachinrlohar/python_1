#!/bin/bash
python3 hist_kmers.py kmers.txt bins.txt Sample_Sequences.fa

# hist_kmer.py program takes three command-line arguments, a k-mer list file, 
# a file defining the histogram bins and a file of sequences. Any number of 
# sequence files can be given through CLI.


# This program computes the distribution of occurrences of these motifs in a set 
# of DNA sequences and print to a seperate output file for each motif.

# File 1 - K-mer list file
# File 2 - Bin file
# File 3 - Sequence files
