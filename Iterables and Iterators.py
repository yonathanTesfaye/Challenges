# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

rang = int(input())
letters = input().split()
slic = int(input())
combs = list(combinations(letters,slic))
length = len(combs)
prob=0
for comb in combs:
    if 'a' in comb:
        prob +=1
print(f'{prob/length:.3f}')
