import Bio.SeqIO
# translating all possible open reading frames of a protein sequence from a
#given string, including the complement strand.
def codons(seq,frame): #requires a provided sequence and the frame of interest(frames being 1,2, or 3
    n = len(seq) #gets length of the sequence
    #print(n)
    cdns = []
    for i in range(frame - 1, n - 2, 3): #starts at (frame of interest) - 1, ends at (n-2) to prevent dicodons, and steps every 3.
        cdns.append(seq[i:i+3])
        #yield seq[i:i+3] #yields in specific and returns a generator object. Changed because it got rough after this
    return cdns
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
def orftranslate(seq):
    orflibrary = []  # list of translated orf
    for frm in range(1, 4): #range() is exlusive on the end, so it needed to be 4
        codonlist = codons(seq, frm) #populates codonlist with the codons of that frame
        #print(codonlist)
        for n in range(len(codonlist)):
            if codonlist[n] == 'ATG':
                templist = codonlist[n:]
                #print(templist)
                currentorf = []
                for codon in templist:
                    if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
                        break
                    else:
                        currentorf.append(aadict[codon])
                aaframe = "".join(currentorf)
                orflibrary.append(aaframe)
            else:
                continue
    #for read in orflibrary:
        #print(read)
    return orflibrary
for record in Bio.SeqIO.parse('rosalind_orf.txt', "fasta"):
    fileseq = record.seq

rev_fileseq = reverse_sequence(fileseq)
#print("reverse sequence", rev_fileseq)
aadict = get_lookup()
#orftranslate(fileseq)
#orftranslate(rev_fileseq)
final = orftranslate(fileseq)
final.extend(orftranslate(rev_fileseq))
for protein in set(final):
    print(protein)