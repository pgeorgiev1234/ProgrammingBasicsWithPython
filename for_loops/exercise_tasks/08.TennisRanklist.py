import math

tournirs = int(input())
points = int(input())

wins = 0
avg = 0
for i in range (0,tournirs):
    a = input()
    if a == "W":
        wins+=1
        points+=2000
        avg+=2000
    elif a == "F":
        points+=1200
        avg+=1200
    elif a == "SF":
        points+=720
        avg+=720

print(f"Final points: {points}")
print(f"Average points: {math.floor(avg/tournirs):.0f}")
print(f"{wins/tournirs*100:.2f}%")