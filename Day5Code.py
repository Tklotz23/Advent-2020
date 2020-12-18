# LOL Part 1 is just converting the data into binary pairs.
import string
seat_assign=open('Day5Data.txt').read()
seat_assign_split=seat_assign.split('\n')
seat_assign_split.remove('')
# Should prolly add some more comments. The following functions just straight-up converts each seat assignement to a row number and collumn number and returns the unique seat ID defiend in the problem. 
def id_calc(letters):
    row=0
    column=0
    for i in range(len(letters)):
        if letters[i]=='B':
            row=row+2**(6-i)
        if letters[i]=='R':
            column=column+2**(9-i)
    return 8*row+column
# Cool, cool. Now just to initialize some stuff. I make a mildly pointless dictionary to store the seat IDs of each seat assignment as a key with seat assignement the corresponding value. I also intialize some variables for max and min seat IDs. 
seat_id_max=0
id_dict={}
for i in seat_assign_split:
    seat_id_max=max(seat_id_max,id_calc(i))
    id_dict[id_calc(i)]=i
print(seat_id_max)
seat_id_min=seat_id_max
for i in seat_assign_split:
    seat_id_min=min(seat_id_min,id_calc(i))
# To get my seat ID I just cycle through all possible seat IDs and see which are missing. Turns out to be unique in this case. 
for i in range(seat_id_min, seat_id_max):
    if id_dict.get(i)==None:
        print(i)
