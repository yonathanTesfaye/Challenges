# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

items = int(input())
ordered_dictionary = OrderedDict()

for item in range(items):
    infos = input().split()
    infos = tuple(infos)
    key = infos[:len(infos)-1]
    value = int(infos[len(infos)-1])
    if key in ordered_dictionary:
        ordered_dictionary[key] += value
    else:
        ordered_dictionary[key] = value
for key,value in ordered_dictionary.items():    
    print(*key,value)
