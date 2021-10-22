#rabbits man
#given n and k. n is time target, or number of iterations to perform, and k is the number of 'pairs' m+f
#that are born per litter. Seems like a recursion problem, where it will call itself n times, and values
#increase by k
def rabbits(k):
    off_spring = k

    pop.append(pop[-1]+(pop[-2]*int(k)))

try:
    with open("rosalind_fib.txt", "r") as my_file:
        line = my_file.read()
        line = line.replace('\n', '')
        nums = line.split(' ')
        for thing in nums:
            print(thing)
except IOError as err:
    print(err)
pop = [1, 1]
for i in range(int(nums[0])-2):
    rabbits(nums[1])
print(pop[-1])
