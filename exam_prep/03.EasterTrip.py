country = input()
period = input()
days = int(input())

suma = 0
if country == "France":
    if period == "21-23":
        suma = days*30
    elif period == "24-27":
        suma = days*35
    else:
        suma = days*40
elif country == "Italy":
    if period == "21-23":
        suma = days * 28
    elif period == "24-27":
        suma = days * 32
    else:
        suma = days * 39
elif country == "Germany":
    if period == "21-23":
        suma = days * 32
    elif period == "24-27":
        suma = days * 37
    else:
        suma = days * 43

print(f"Easter trip to {country} : {suma:.2f} leva.")