import math

form = input()

if form == "square":
    a = float(input())
    print(f"{a*a:.3f}")
elif form =="rectangle":
    a = float(input())
    b = float(input())
    print(f"{a*b:.3f}")
elif form == "circle":
    a=float(input())
    print(f"{a*a*math.pi:.3f}")
elif form=="triangle":
    a=float(input())
    b=float(input())
    print(f"{a*b/2:.3f}")
    