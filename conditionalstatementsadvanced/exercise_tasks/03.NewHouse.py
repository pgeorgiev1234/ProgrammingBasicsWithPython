flower=input()
quantity = int(input())
budget = int(input())

suma = 0

if flower=="Roses":
    suma=quantity*5
    if quantity>80:
        suma*=0.9
elif flower=="Dahlias":
    suma=quantity*3.8
    if quantity>90:
        suma*=0.85
elif flower=="Tulips":
    suma=2.80*quantity
    if quantity>80:
        suma*=0.85
elif flower=="Narcissus":
    suma=3*quantity
    if quantity<120:
        suma*=1.15
elif flower=="Gladiolus":
    suma=2.50*quantity
    if quantity<80:
        suma*=1.2

if suma >budget:
    print(f"Not enough money, you need {suma-budget:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {quantity} {flower} and {budget-suma:.2f} leva left.")
