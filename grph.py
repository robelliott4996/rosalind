#from a series of fasta files, generate the adjacency list.
#the last 3 bases of string s should be the first three bases of string t.
# so long as s is not the same string as t.

import Bio.SeqIO #to read fasta file

entrydict = {}
for record in Bio.SeqIO.parse('rosalind_grph.txt', "fasta"):
    entrydict[record.id] = record.seq

#store results in a dictionary for printing.