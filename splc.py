#given string s representing the full dna, slice out the introns, concatenate the exons, and translate
#will be fasta format, first string is total dna. Following entries are introns, indeterminate number.
#extension of finding motiffs but instead of simple reporting the position, need to slice it out.
#Need to loop for each intron, one at a time.
#remember to account for pythons 0-based indexing feature
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
    print(n)
    for i in range(frame - 1, n - 2, 3):
        yield seq[i:i+3]

dna_seq = '' # first object is main string, second is motiff string
introns = []
all_seqs = []
for record in Bio.SeqIO.parse("rosalind_splc.txt", "fasta"):
    all_seqs.append(record.seq)
dna_seq = all_seqs[0]
introns = all_seqs[1:]
#removing introns from dna
for intron in introns: #for each intron
    for i in range(len(dna_seq)): #iterate through the main sequence until...
        if intron == dna_seq[i:i+len(intron)]: #the intron and the comparable slice of the main seq are equivalent
            dna_seq = dna_seq.replace(dna_seq[i:i+len(intron)],"") #and then replace that slice with 'nothing'
        else:
            continue
#translating dna to protein
rna_seq = dna_seq.replace('T', 'U') #quick switch from dna to rna
peptide = []
rna_codons = codons(rna_seq, 1)
rna_to_aadict = rna_to_aa()
for triplet in rna_codons:
    peptide.append(rna_to_aadict[triplet])
print(''.join(peptide))
