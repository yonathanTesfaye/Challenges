# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

inst = list(input().split())

for rang in range(1,int(inst[1])+1):
    lst = list(combinations(inst[0],rang))
    if rang == 1:
        lst1 = sorted(lst)
        for first in lst1:
            print(*first)

    else:
        lstx =list()
        for i in lst:
            lst2 = sorted(i)
            lstx.append(lst2)
        #print(lstx)
        srted_lst = sorted(lstx)       
        for last in srted_lst:
            print(*last, sep='')
        
    
