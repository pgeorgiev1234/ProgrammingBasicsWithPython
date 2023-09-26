budget = float(input())
statist= int(input())
price_costume= float(input())

sum_decor = 0.1*budget
sum_costumes = statist*price_costume
sum_costumes = 0.9*sum_costumes if statist>150 else sum_costumes
sum_film = sum_decor+sum_costumes

if sum_film<=budget:
    print(f"Action!\nWingard starts filming with {budget-sum_film:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {sum_film-budget:.2f} leva more.")
