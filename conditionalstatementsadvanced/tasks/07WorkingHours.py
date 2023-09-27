time = int(input())
day = input()

if day == "Sunday":
    print("closed")
else:
    if 10 <= time <= 18:
        print("open")
    else:
        print("closed")
