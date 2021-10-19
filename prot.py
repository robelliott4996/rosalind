#translating a RNA string into AA string

import Bio.SeqIO

def rna_to_aa():
    return {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
            'UAU':'Y', 'UAC':'Y', 'UAA':'*', 'UAG':'*', 'UGU':'C', 'UGC':'C', 'UGA':'*', 'UGG':'W',
            'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
            'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
            'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
            'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
            'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
            'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

def codons(seq,frame):
    n = len(seq)
    for i in range(frame - 1, n - 2, 3):
        yield seq[i:i+3]


rna_to_aadict = rna_to_aa()
rna_string = ''
for record in Bio.SeqIO.parse('rosalind_prot.txt', 'fasta'):
    rna_string = record.seq
peptide = []
rna_codons = codons(rna_string, 1)
for triplet in rna_codons:
    peptide.append(rna_to_aadict[triplet])
print(''.join(peptide))
