# Aight. Day 3, Tobbagan tree dodgin'. Classic. 
import string
import math
tree_map=open("Day3Data.txt").read()
tree_map_split=tree_map.split("\n")
tree_map_split.remove('')
width=len(tree_map_split[1])
depth=len(tree_map_split)
print(width, depth)
line11_string=''
line31_string=''
line51_string=''
line71_string=''
line12_string=''
for i in range(depth):
    line11_string+=tree_map_split[i][i%width]
    line31_string+=tree_map_split[i][3*i%width]
    line51_string+=tree_map_split[i][5*i%width]
    line71_string+=tree_map_split[i][7*i%width]
for i in range(depth//2):
    line12_string+=tree_map_split[2*i][i%width]
print(line11_string.count('#')*line31_string.count('#')*line51_string.count('#')*line71_string.count('#')*line12_string.count('#'))

