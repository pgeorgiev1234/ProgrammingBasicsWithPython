n = int(input())

p1=0
p2=0
p3=0
p4=0
p5=0

for i in range (0,n):
    a = int(input())
    if a <=5:
        p1+=a
    elif a <=12:
        p2+=a
    elif a <=25:
        p3+=a
    elif a <=40:
        p4+=a
    else:
        p5+=a

total = p1+p2+p3+p4+p5
print(f"{p1/total*100:.2f}%")
print(f"{p2/total*100:.2f}%")
print(f"{p3/total*100:.2f}%")
print(f"{p4/total*100:.2f}%")
print(f"{p5/total*100:.2f}%")