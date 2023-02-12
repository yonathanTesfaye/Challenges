# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
nums = groupby(input())
for num,key in nums:
    print((len(list(key)),int(num)), sep=', ',end=' ') 
