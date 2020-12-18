# Okay here we go. Advent 2020 Day 1.....Only 2 weeks late! 
#Aight, importing numpy 'cause why not I guess
import numpy
import string
# now. I've got to figure out how to find a pair of numbers in a in a file that add up to 2020 and then I need to take their product. Should be easy enough.
Numbahs=open("Day1Data.txt").read()
numbahs=Numbahs.split("\n")
# Okay, so numbahs has a mysterious extra token at the end. Make sure to account for this when converting to an int list. 
numbahs.remove('')
numbahs=[int(i) for i in numbahs]
# Okay. Now I gots a list of numbahs. Time to check for summing to 2020. 
for i in numbahs: 
    if 2020-i in numbahs:
        mult_pair=(2020-i)*i
        num_pair_check=[2020-i,i]
    for j in numbahs:
        if 2020-i-j in numbahs:
            mult_tri=(2020-i-j)*i*j
            num_tri_check=[2020-i-j,i,j]
print(num_pair_check)
print(mult_pair)
print(num_tri_check)
print(mult_tri)
