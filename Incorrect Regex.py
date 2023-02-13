# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

num = int(input())
for n in range(num):
    T = input()
    try:
        re.compile(T)
        print(True)
    except re.error:
        print(False)
