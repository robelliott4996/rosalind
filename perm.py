#given a positive integer n, return the number of possible permutations of the numbers 1->n and list them
#recursion? Call the function n times,
import random
import math
try:
    with open("rosalind_perm.txt", "r") as my_file:
        lines = my_file.readlines()
        num = int(lines[0].rstrip())
except IOError as err:
    print(err)
print(num)
numbers = []
perm_dict = [] #not actually a dictionary
print(math.factorial(num))
for n in range(1,num+1):
    numbers.append(n)
while len(perm_dict) < math.factorial(num):
    temp_list = numbers
    permutation = []
    while len(permutation) < num:
        temp_item = str(random.choice(temp_list))
        if temp_item not in permutation:
            permutation.append(temp_item)
        else:
            continue
    if " ".join(permutation) in perm_dict:
        continue
    else:
        perm_dict.append(" ".join(permutation))
        print(" ".join(permutation))

#need to just print to a file, can't copy/paste easily anymore
try:
    with open("rosalind_perm_output.txt", "w") as outputfile:
        outputfile.write("{}\n".format(math.factorial(num)))
        for thing in perm_dict:
            outputfile.write("{}\n".format(thing))
    outputfile.close()
except IOError as err:
    print(err)
