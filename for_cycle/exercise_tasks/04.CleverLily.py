age=int(input())
price_laundry=float(input())
price_toy = int(input())

suma=0
podaruk = 9

for i in range (1,age+1):
    if i%2==1:
        suma+=price_toy
    else:
        suma+=podaruk
        podaruk+=10

if suma >= price_laundry:
    print(f"Yes! {suma-price_laundry:.2f}")
else:
    print((f"No! {price_laundry-suma:.2f}"))
