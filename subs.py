#remember to account for pythons 0-based indexing feature
seq = [] # first object is main string, second is motiff string
try:
    with open("rosalind_subs.txt", 'r') as my_file:
        for line in my_file:
            seq.append(line[:-1:])
            #print(line)
except IOError as err:
    print(err)
position = []
for i in range(len(seq[0])):
    if seq[1] == seq[0][i:i+len(seq[1])]:
        position.append(i+1)
    else:
        continue

print(position)
