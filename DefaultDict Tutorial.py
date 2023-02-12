# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

inpt = list(map(int, input().split()))
lstA = list()
di = defaultdict(list)

for rang1 in range(inpt[0]):
    di[input()].append(rang1+1)

for rang2 in range(inpt[1]):
    m = input()
    if m in di.keys():
        for key, value in di.items():
            if m == key:
                print(*value)
    else:
        print(-1)
                
