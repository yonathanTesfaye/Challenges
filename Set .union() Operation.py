# Enter your code here. Read input from STDIN. Print output to STDOUT
class1 = int(input())
roll1 = set(map(int,input().split()))
class2 = int(input())
roll2 = set(map(int,input().split()))
union = roll1|roll2
print(len(union))
