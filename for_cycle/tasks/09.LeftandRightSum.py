n = int(input())
sumaleft = 0
sumaright=0

for i in range(0,n):
    a=int(input())
    sumaleft+=a

for i in range(0,n):
    a = int(input())
    sumaright+=a

if sumaleft==sumaright:
    print(f"Yes, sum = {sumaleft}")
else:
    print(f"No, diff = {abs(sumaleft-sumaright)}")