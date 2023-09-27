city = input()
sales = float(input())

if city == "Sofia":
    if sales<0:
        print("error")
    elif sales>=0 and sales<=500:
        print(f"{0.05*sales:.2f}")
    elif sales>500 and sales<=1000:
        print(f"{0.07*sales:.2f}")
    elif sales>1000 and sales<=10000:
        print(f"{0.08*sales:.2f}")
    else:print(f"{0.12*sales:.2f}")
elif city == "Varna":
    if sales<0:
        print("error")
    elif sales>=0 and sales<=500:
        print(f"{0.045*sales:.2f}")
    elif sales>500 and sales<=1000:
        print(f"{0.075*sales:.2f}")
    elif sales>1000 and sales<=10000:
        print(f"{0.1*sales:.2f}")
    else:print(f"{0.13*sales:.2f}")
elif city == "Plovdiv":
    if sales < 0:
        print("error")
    elif sales >= 0 and sales <= 500:
        print(f"{0.055 * sales:.2f}")
    elif sales > 500 and sales <= 1000:
        print(f"{0.08 * sales:.2f}")
    elif sales > 1000 and sales <= 10000:
        print(f"{0.12 * sales:.2f}")
    else:
        print(f"{0.145 * sales:.2f}")
else:print("error")
