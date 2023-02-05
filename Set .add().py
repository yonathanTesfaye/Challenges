# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
set1 = set()
for i in range(N):
    S = input()
    set1.add(S)  
print(len(set1))
