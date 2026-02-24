import math

c = float(input())
radian = c * math.pi / 180
print(round(radian, 6))




print("-"*100)
h = 5.0
b1 = 5.0
b2 = 6.0
area = (b1 + b2) * h / 2
print(area)




print("-"*100)
n = int(input())
s = float(input())
area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print(int(area))




print("-"*100)
base = 5.0
height = 6.0
area = base * height
print(float(area))