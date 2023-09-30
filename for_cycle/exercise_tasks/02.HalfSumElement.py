import sys

n = int(input())

suma = 0
max = -sys.maxsize
for i in range(0,n):
    a = int(input())
    suma+=a
    if a>max:
        max=a

if max==suma-max:
    print(f"Yes\nSum = {suma-max}")
else:
    print(f"No\nDiff = {abs((suma-max)-max)}")
