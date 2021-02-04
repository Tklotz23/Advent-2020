# Day 6 here we go. Counting up yesses for customs checks. Part 1 should be easy-peasy-lemon tart or something. 
# Part 1
from collections import Counter
import string
groups=open('Day6Data.txt').read()
groups_split=groups.split('\n\n')
groups_split_new=[]
for i in groups_split:
    groups_split_new.append(i.replace('\n',' '))
# Anticipating doing stuff I don't know about yet in part 2 I decided to through this all into a dictionary with keys given by the elements of groups_split_new and values given by the number of yesses in each group. 
answers_dict={}
for i in groups_split_new:
    counter=0
    for j in string.ascii_lowercase:
        if j in i:
            counter+=1 
    answers_dict[i]=counter
# Problem wants me to add up all the yesses so....
print(sum(answers_dict.values()))
# Part 2
# LOL my dictionary is pointless for part 2 haha
counter_list=[]
groups_split_newx2=[]
for i in groups_split_new:
    i=i.strip(' ')
    groups_split_newx2.append(i)
for i in groups_split_newx2:
    counter=0
    group_size=i.count(' ')+1
    print(group_size)
    for j in string.ascii_lowercase:
        if i.count(j)==group_size:
            counter+=1
    counter_list.append(counter)
print(sum(counter_list))

