s = "CTCAGTGCGACCTGGGAATATTACTGTTCCTTGCCCTCTTGTAATACCCTCAAGATGCATCGTACGTACCGTTCACATTTATAATTAGAGGTACACGCTCCTACTGCTGGTCTCGTCATGTGATTGTCGCGAAGCTGAGGATAAATAACTGACAGCAGCGCGGAAAGCATTTATAAGTATTATCACTTCGTGTTTTGCCGATAACGGTCACGGCGTGCTTAAGATCGGACTCTTGGTATTTATCTGCACGTATATGCGCAGGCGCACGCACCCGAATAACATAGCCCTTCTGGCATGGCAGTAATAGGAATTAGGCTCTAGTTAGTCAGTCCCTAGTTATACACAACAATACAGGCGCATTTGCTACGGACAGTGTCGTTAAAATAGGCAGTTTAAAGACGGCGAACTAGTATCGGGTGCTTTCGGTGCGGCATCGTCCGTCATTGGACGGCCTGCTCTTGTTCTGTAGATTAGCGCCCAAACCATATTTGTGTTGGTCAGACTACACTACCGATCGGGCCCACCTGGTTAATGAATCACCGCGGCCGCGATTGCATATAGTCCTAAGCGGGAGGCAATCGGATATCAGAAGAAGATAACTATGCGCGGTTGCCGGGACCGTTATGGTTACTCTCTCACGGCGATTATGTCATTCCCCATCGGGCCCGGCTTACATTTCGTGATCGCTCAGTGGAGGGCATCTCTACTCTCGGTGAATCGAATGCCCCTAAATGCGGGGTGCTATACAACCTGCTGTACGGACGATCATCCACATTACTCTCTCTATGTGAGTGCAAACCAGATTGCAAAGCAGCCTCCGAATTCTCGCAATCCATCAGTTGAGCCGTGGGCGTAGCGCAGCCGCGATGCTTCCGTTATGGTTCCGAGGGAGAAAATGCGGGAAAACCGAACCCGCGGGAGACGCAGTTAGCAAGGAGAGCTTATGCAAAAAGACGTTTTACCTC"
comp = []
for nuc in s[::-1]:
	if nuc == "A":
		comp.append("T")
	if nuc == "T":
		comp.append("A")
	if nuc == "C":
		comp.append("G")
	if nuc == "G":
		comp.append("C")
sc = "".join(comp)
print(sc)