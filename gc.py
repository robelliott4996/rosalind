# for DNA in Rosalind project in python
import Bio.SeqIO

id = ''
gc_count = 0

for record in Bio.SeqIO.parse("rosalind_gc.txt", "fasta"): #only using Biopython for its fasta reading capability
    g = 0
    c = 0
    a = 0
    t = 0
    nucs = 0
    for nuc in record.seq:
        if nuc == "G":
            g += 1
            nucs += 1
        if nuc == "C":
            c += 1
            nucs += 1
        if nuc == "A":
            a += 1
            nucs += 1
        if nuc == "T":
            t += 1
            nucs += 1
    if (((g + c) / nucs)*100) > gc_count:
        id = record.id
        gc_count = round((((g + c) / nucs)*100), 6) #need to make this have only 6 decimals

print("{}\n{}".format(id, gc_count))
