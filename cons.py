#from a provided set of DNA strings. Create a profile matrix and determine the consensus sequence
#provided in fasta format
import random
import Bio.SeqIO
entrydict = {} #for storing the fasta sequence, May not need this if I only have to iterate through each sequence once
profiledict = {"A":[], "C":[], "T":[],"G":[]} #Keys are nucleotides. object is list of sequence position.
#initially, nucletoides object lists need to be a list of zeros the same length as the dna strings

for record in Bio.SeqIO.parse('rosalind_cons.txt', "fasta"):
    entrydict[record.id] = record.seq
for n in range(len(random.choice(list(entrydict.values())))):#picks a random value from the dictionary
    profiledict["A"].append(0)
    profiledict["C"].append(0)
    profiledict["T"].append(0)
    profiledict["G"].append(0) #populates with zeros equal to length of sequences.
for entry in entrydict:
    for n in range(len(entrydict[entry])):
        if entrydict[entry][n] == "A":
            profiledict["A"][n] += 1
        if entrydict[entry][n] == "C":
            profiledict["C"][n] += 1
        if entrydict[entry][n] == "T":
            profiledict["T"][n] += 1
        if entrydict[entry][n] == "G":
            profiledict["G"][n] += 1
consensus = [] #emtpy list to hold nucleotide sequence
seqlength = len(random.choice(list(entrydict.values())))
for n in range(len(random.choice(list(entrydict.values())))):
    nuc = ''
    nuccount = 0
    for nucleotide in profiledict: #iterate through each nucleotide profile and access nth item
        if profiledict[nucleotide][n] > nuccount:
            nuc = nucleotide #need to change nuc value to associated nucleotide
            nuccount = profiledict[nucleotide][n]
    consensus.append(nuc)
seperator = " "
print("".join(consensus))
print("{}: {}".format('A', seperator.join(map(str, profiledict["A"]))))
print("{}: {}".format('C', seperator.join(map(str, profiledict["C"]))))
print("{}: {}".format('G', seperator.join(map(str, profiledict["G"]))))
print("{}: {}".format('T', seperator.join(map(str, profiledict["T"]))))