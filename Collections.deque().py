# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

num = int(input())
d = deque()
for n in range(num):
    inst = input().split()
    if inst[0]=='append':
        d.append(int(inst[1]))
    elif inst[0]=='pop':
        d.pop()
    elif inst[0]=='popleft':
        d.popleft()
    elif inst[0]=='appendleft':
        d.appendleft(int(inst[1]))
print(*d)
