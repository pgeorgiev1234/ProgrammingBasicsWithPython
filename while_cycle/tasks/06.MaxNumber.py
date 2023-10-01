import sys
max = -sys.maxsize

while True:
    line = input()
    if line=="Stop":
        break
    number=int(line)
    if number>max:
        max=number

print(max)