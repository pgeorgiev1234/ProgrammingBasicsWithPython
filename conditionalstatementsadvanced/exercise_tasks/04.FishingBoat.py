budget = int(input())
season = input()
fishermen = int(input())

total_sum = 0

if season == "Spring":
    total_sum += 3000
elif season == "Summer":
    total_sum += 4200
elif season == "Autumn":
    total_sum += 4200
elif season == "Winter":
    total_sum += 2600

if fishermen <= 6:
    total_sum *= 0.9
elif 6 < fishermen <= 11:
    total_sum *= 0.85
else:
    total_sum *= 0.75

if fishermen % 2 == 0 and season != "Autumn":
    total_sum *= 0.95

if total_sum <= budget:
    print(f"Yes! You have {budget - total_sum:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva.")
