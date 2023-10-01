vhod = input()
suma=0

while vhod!="NoMoreMoney":
    number=float(vhod)
    if number>=0:
        print(f"Increase: {number:.2f}")
        suma +=number
    else:
        print("Invalid operation!")
        break
    vhod=input()

print(f"Total: {suma:.2f}")
