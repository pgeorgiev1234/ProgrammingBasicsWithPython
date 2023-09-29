import sys

n = int(input())

max = -sys.maxsize
min = sys.maxsize

for i in range (0, n ):
    a = int(input())
    if a>max:
        max=a
    if a<min:
        min=a

print(f"Max number: {max}")
print(f"Min number: {min}")