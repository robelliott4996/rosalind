#from a series of fasta files, generate the adjacency list.
#the last 3 bases of string s should be the first three bases of string t.
# so long as s is not the same string as t.

import Bio.SeqIO #to read fasta file

entrydict = {}
resultlist = []
for record in Bio.SeqIO.parse('rosalind_grph.txt', "fasta"):
    entrydict[record.id] = record.seq
    #print(record.id, record.seq)
for first in entrydict:
    for second in entrydict:
        if entrydict[first][-3:] == entrydict[second][:3:] and first != second:
            #insert into resultslists
            resultlist.append((first, second))

        else:
            continue
#store results in a dictionary for printing.
for result in resultlist:
    print("{} {}".format(result[0], result[1]))

    #results were very long, should've printed to a file