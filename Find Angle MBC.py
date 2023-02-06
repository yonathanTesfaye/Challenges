# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = float(input())
BC = float(input())

angle = math.atan(AB/BC)

AC = math.sqrt(pow(AB,2)+pow(BC,2))
MC = AC/2

BM = math.sqrt(pow(MC,2)+pow(BC,2)-(2*BC*MC*math.cos(angle)))

Angle = (MC*math.sin(angle))/BM
Angle = math.asin(Angle)
Angle = math.degrees(Angle)
Angle = round(Angle)
Angle = str(Angle)+'\u00b0'
print(Angle)
