#mendelien inheritance and probability
#Probability two random organisms mate and produce individual
#with a dominant allele
#would be better to create a punnet square calculator for population simulation I think
try:
    with open("rosalind_iprb.txt", "r") as my_file:
        lines = my_file.readlines()
        values = lines[0].split(' ') #list with each individual value
except IOError as err:
    print(err)
a = float(values[0])  #individuals homo dominant
b = float(values[1]) #individuals hetero
c = float(values[2]) #individuals homo recessive

def prob_dom(k,m,n):
    t = k+m+n
    pk = k/t
    pm = m/t
    pn = n/t
    prob = 1 - pm*((m-1)/(t-1))*0.25 - 2*pn*(m/(t-1))*0.5 - pn*((n-1)/(t-1))

    return prob
print(prob_dom(a,b,c))
