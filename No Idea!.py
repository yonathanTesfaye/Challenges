# Enter your code here. Read input from STDIN. Print output to STDOUT
range_tellers = list(map(int, input().split()))
lst = list(map(int, input().split()))
sets1 = set((map(int, input().split())))
sets2 = set((map(int, input().split())))

counter=0
for num in lst:
    if num in sets1:
        counter +=1
    elif num in sets2:
        counter -=1
print(counter)

  

           
