# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations 
inst = list(input().split())
result = list(permutations(inst[0],int(inst[1])))
if int(inst[1]) ==1:
    srted_lst = sorted(result)
    for i in srted_lst:
        print(*i)
else:
    srted_lst0 = sorted(result, key=lambda x:(x[0], x[1]))
    for i in srted_lst0:
        print(*i, sep='')
