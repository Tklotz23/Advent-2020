# Day 4 passport fudgin'. Here we go! 
#Completely rewriting from my Part 1 Solution so I can call functions. 

# Part 1

import string
p_batch=open('Day4Data.txt').read()
p_batch_split=p_batch.split('\n\n')
p_batch_new=[]
p_fields=['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
p_fields_new=['byr','iyr','eyr','hgt','hcl','ecl','pid']
p_batch_refined=[]
for i in p_batch_split:
    p_batch_new.append(i.replace('\n',' '))
counter=0
for i in p_batch_new:
    counter=0
    for j in p_fields_new:
        if j in i:
            counter+=1
    if counter==7:
        # This part below makes a new batch of valid passports. That is each individual passport is an element of the list p_batch_refined.
        p_batch_refined.append(i)
print(len(p_batch_refined))

# Part 2

# Dictionary time! First time using dictionaries in python so naturally I go with a dictionary of dictionaries (batch_dict could just be a list but I wanted to use the delete option for a dictionary later on just 'cause). Each inner dict (field_dict) in batch_dict assigns the data of an individual passport to its corresponding field. 
batch_dict={}
for i in p_batch_refined:
    field_dict={}
    for j in p_fields_new:
        field_loc=i.find(j)+len(j)+1
        if i.find(' ',field_loc)==-1:
            field_space_loc=len(i)
        else:
            field_space_loc=i.find(' ',field_loc)
        field_data=''
        for k in range(field_loc,field_space_loc):
            field_data+=i[k]
        field_dict[j]=field_data
    batch_dict[p_batch_refined.index(i)]=field_dict

# Gotta make some passport data checking functions. Then I make a big function that eats in a dictionary that will return True if all data in the field_dict is valid. 
def hgt_check(height):
    if 'cm' in height:
        hgt_num=int(height.replace('cm',''))
        return hgt_num>=150 and hgt_num<=193
        
    if 'in' in height:
        hgt_num=int(height.replace('in',''))
        return hgt_num>=59 and hgt_num<=76

def hcl_check(hair_color):
    len_req=6
    if '#' in hair_color:
        color_hex=hair_color.replace('#','')
        sub_counter=0
        for s in color_hex:
            if s in string.hexdigits:
                sub_counter+=1
        return sub_counter==len_req

def ecl_check(eye_color):
    color_options=['amb','blu','brn','gry','grn','hzl','oth']
    return eye_color in color_options

def pid_check(p_id):
    len_req=9
    int_string='0123456789'
    sub_counter=0
    for s in p_id:
        if s in int_string:
            sub_counter+=1
    return sub_counter==len_req

# This is the dictionary eating function previously mentioned. 
def p_checker(data_dict):
    counter=0
    b_year=int(data_dict[p_fields_new[0]])
    if b_year>= 1920 and b_year<= 2002:
        counter+=1
    i_year=int(data_dict[p_fields_new[1]])
    if i_year>= 2010 and i_year<= 2020:
        counter+=1
    e_year=int(data_dict[p_fields_new[2]])
    if e_year>= 2020 and e_year<= 2030:
        counter+=1
    if hgt_check(data_dict[p_fields_new[3]]):
        counter+=1
    if hcl_check(data_dict[p_fields_new[4]]):
        counter+=1
    if ecl_check(data_dict[p_fields_new[5]]):
        counter+=1
    if pid_check(data_dict[p_fields_new[6]]):
        counter+=1
    return counter==len(p_fields_new)

# Okay now to pass each field_dict into p_checker and then remove said field_dict from batch_dict if it is invalid.
for key in range(len(p_batch_refined)):
    if not p_checker(batch_dict[key]):
        del batch_dict[key]
print(len(batch_dict))




