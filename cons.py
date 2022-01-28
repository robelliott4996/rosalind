#from a provided set of DNA strings. Create a profile matrix and determine the consensus sequence
#provided in fasta format

import Bio.SeqIO
entrydict = {} #for storing the fasta sequence, May not need this if I only have to iterate through each sequence once
profdict = {"A":[], "C":[], "T":[],"G":[]} #Keys are nucleotides. object is list of sequence position
for record in Bio.SeqIO.parse('rosalind_cons.txt', "fasta"):
    for n in range(len(record.seq)):


#for key in entrydict:
#    print(entrydict[key])