import sys
min = sys.maxsize

while True:
    line = input()
    if line=="Stop":
        break
    number=int(line)
    if number<min:
        min=number

print(min)