# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

rang = int(input())
lst = map(int, input().split())
count = Counter(lst)
customers = int(input())
lst = list()
sum=0
for customer in range(customers):
    purchases = list(map(int, input().split()))
    lst.append(purchases)
for buy in lst:
    if buy[0] in count.keys():
        #print(buy)
        if count[buy[0]]>=1:
            sum+=buy[1]
            count[buy[0]]-=1
print(sum)
