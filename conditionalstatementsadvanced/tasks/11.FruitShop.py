fruit = input()
day = input()
quantity = float(input())

if day == "Monday" or day =="Tuesday" or day =="Wednesday" or day =="Thursday" or day =="Friday":
    if fruit =="banana":
        print(f"{2.5*quantity:.2f}")
    elif fruit == "apple":
        print(f"{1.2*quantity:.2f}")
    elif fruit == "orange":
        print(f"{0.85*quantity:.2f}")
    elif fruit == "grapefruit":
        print(f"{1.45*quantity:.2f}")
    elif fruit == "kiwi":
        print(f"{2.7*quantity:.2f}")
    elif fruit == "pineapple":
        print(f"{5.5*quantity:.2f}")
    elif fruit == "grapes":
        print(f"{3.85*quantity:.2f}")
    else:print("error")
elif day == "Saturday" or day=="Sunday":
    if fruit == "banana":
        print(f"{2.7*quantity:.2f}")
    elif fruit == "apple":
        print(f"{1.25*quantity:.2f}")
    elif fruit == "orange":
        print(f"{0.9*quantity:.2f}")
    elif fruit == "grapefruit":
        print(f"{1.6*quantity:.2f}")
    elif fruit == "kiwi":
        print(f"{3*quantity:.2f}")
    elif fruit == "pineapple":
        print(f"{5.6*quantity:.2f}")
    elif fruit == "grapes":
        print(f"{4.2*quantity:.2f}")
    else:
        print("error")
else:
    print("error")
