# Enter your code here. Read input from STDIN. Print output to STDOUT
lst1 = list()
lst2 = list()
lst3 = list()
def sym_dif(a,b):
    a = set1.difference(set2)
    b = set2.difference(set1)
    lst3.extend(a)
    lst3.extend(b)
    srted_lst = sorted(lst3)
    for num in srted_lst:
        print(num)  
     
     
M = int(input())
a = input()
lst1 = a.split(' ')
lst1 = list(map(int,lst1))
set1 = set(lst1)
N = int(input())
b = input()
lst2 = b.split(' ')
lst2 = list(map(int,lst2))
set2 = set(lst2)
difference = sym_dif(a,b)
