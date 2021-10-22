#calculating hamming distance.
#split sequences into individual characters. Use tuples, make set of tuples, and do set manipulation
# to get number of differences
s = ''
t = ''
try:
    with open('rosalind_hamm.txt', 'r') as my_file:
        lines = my_file.readlines()
        s = lines[0].replace('\n', '')
        t = lines[1].replace('\n', '')
except IOError as err:
    print(err)

s_tuples = []
t_tuples = []
for position in range(len(s)):
    s_tuples.append((s[position], position))
for position in range(len(t)):
    t_tuples.append((t[position], position))

nuc_diff = set(s_tuples).symmetric_difference(set(t_tuples))
print(len(nuc_diff)/2)
#print(s_tuples)
#print(t_tuples)
#print(nuc_diff)
