month = input()
nights = int(input())

sum_apartment = 0
sum_studio = 0

if month == "May" or month== "October":
    sum_apartment=65*nights
    sum_studio=50*nights
    if 7<nights<=14:
        sum_studio*=0.95
    elif nights>14:
        sum_studio*=0.7
        sum_apartment*=0.9
elif month == "June" or month=="September":
    sum_apartment = 68.7*nights
    sum_studio = 75.2*nights
    if nights > 14 :
        sum_studio*=0.8
        sum_apartment*=0.9
else:
    sum_apartment= 77*nights
    sum_studio = 76*nights
    if nights>14:
        sum_apartment*=0.9

print(f"Apartment: {sum_apartment:.2f} lv.")
print(f"Studio: {sum_studio:.2f} lv.")
