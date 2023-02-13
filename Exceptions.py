# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
for n in range(num):
    try:
        values = list(map(int, input().split()))
        division = values[0]//values[1]
        print(division)
    except ValueError as v:
        print('Error Code:',v)
    except ZeroDivisionError as e:
        print('Error Code:',e)
        
