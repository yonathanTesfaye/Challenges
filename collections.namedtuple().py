# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

students = int(input())
header = namedtuple('student',input())

total = 0
for mark in range(students):
    total+=int(header(*input().split()).MARKS)
print(total/students)
