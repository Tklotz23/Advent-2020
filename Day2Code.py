# Password nonsense. Gotta check some cray-cray password requirements. 
import string
##########################################################################################
# Part 1
passwordinfo=open("Day2Data.txt").read()
passwordinfo_split=passwordinfo.split("\n")
# y u do dis python? I keep getting empty elements at the end of my list. Sigh, guess I gotta handle that nonsense. 
passwordinfo_split.remove('')
# okay fixed. Next I need to split up the elements further. Namely into the key letter, key letter frequency, and passwords themselves.
passwordinfo_splitx2=[]
sub_list=[]
counter= int
counter=0
for i in passwordinfo_split:
    passwordinfo_splitx2.append(i.split(' '))
for i in passwordinfo_splitx2:
    sub_list.append([int(j) for j in i[0].split('-')])
for i in passwordinfo_split:
    loc_string=i.find(':')
    char_at_loc=i[loc_string-1]
    char_count=i.count(char_at_loc)-1
    max_freq=sub_list[passwordinfo_split.index(i)][1]
    min_freq=sub_list[passwordinfo_split.index(i)][0]
    if char_count>=min_freq and char_count<=max_freq:
        counter+=1
print(counter)
##########################################################################################
# Part 2
counter_again= int
counter_again=0
for i in passwordinfo_split:
    loc_string1=i.find(':')
    char_at_loc1=i[loc_string1-1]
    max_exact=sub_list[passwordinfo_split.index(i)][1]+loc_string1+1
    min_exact=sub_list[passwordinfo_split.index(i)][0]+loc_string1+1
    if (i[min_exact]==char_at_loc1 or i[max_exact]==char_at_loc1) and not (i[min_exact]==char_at_loc1 and i[max_exact]==char_at_loc1):
        counter_again+=1
        print(loc_string1,i[min_exact],min_exact,i[max_exact],max_exact,char_at_loc1,passwordinfo_split.index(i))
print(counter_again)
