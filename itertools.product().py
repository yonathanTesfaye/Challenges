# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
AxB = list(product(lst1,lst2))
print(*AxB)
