type_Movie=input()
rows = int(input())
cols = int(input())

income = 0
capacity = cols*rows

if type_Movie=="Premiere":
    income=capacity*12
elif type_Movie == "Normal":
    income=capacity*7.50
else:
    income=capacity*5

print(f"{income:.2f} leva")
