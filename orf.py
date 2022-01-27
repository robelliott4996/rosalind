# translating all possible open reading frames of a protein sequence from a
#given string, including the complement strand.
def codons(seq,frame): #requires a provided sequence and the frame of interest(frames being 1,2, or 3
    n = len(seq) #gets length of the sequence
    #print(n)
    for i in range(frame - 1, n - 2, 3): #starts at (frame of interest) - 1, ends at (n-2) to prevent dicodons, and steps every 3.
        yield seq[i:i+3]
def get_lookup():
    # Obtained from https://stackoverflow.com/questions/19521905/translation-dna-to-protein
    return {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }
def reverse_sequence(seq):
    sequence = seq
    rev_seq = ''
    for nuc in seq:
        if nuc == 'C':
            rev_seq = rev_seq + 'G'
        if nuc == 'G':
            rev_seq = rev_seq + 'C'
        if nuc == 'T':
            rev_seq = rev_seq + 'A'
        if nuc == 'A':
            rev_seq = rev_seq + 'T'
    rev_seq = rev_seq[::-1]  # inverts sequence to so that it's going in the right order
    return rev_seq

aadict = get_lookup()
try:
    with open("rosalind_orf_sample.txt", 'r') as my_file:
        for line in my_file:
            if line.startswith('>'):
                continue
            else:
                fileseq = line #only one fasta entry in this problem
except IOError as err:
    print(err)
print(fileseq)
rev_fileseq = reverse_sequence(fileseq)
print(rev_fileseq)
orflibrary = [] #list of translated orf
for frm in range(1, 3):
    codonlist = codons(seq, frm) #populates codonlist with the codons of that frame
    for n in len(codonlist):
        if codonlist[n] == 'ATG':
            templist = codonlist[n:]
            currentorf = []
            for codon in templist:
                currentorf.append(aadict[codon])
            aaframe = "".join(currentorf)
            orflibrary.append(aaframe)
        else:
            continue


for read in orflibrary:
    print(read)