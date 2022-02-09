#given a positive integer n, return the number of possible permutations of the numbers 1->n and list them

try:
    with open("rosalind_perm.txt", "r") as my_file:
        lines = my_file.readlines()
        num = lines[0].rstrip()
except IOError as err:
    print(err)

print(num)
for n in range(1,6):
    print(n)