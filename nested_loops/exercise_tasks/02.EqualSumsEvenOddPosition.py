num1 = int(input())
num2 = int(input())

for i in range(num1,num2+1):
    suma_even=0
    suma_odd=0
    num=i
    for j in range(0,6):
        if j%2==0:
            suma_even+=num%10
        else:
            suma_odd+=num%10
        num//=10
    if suma_even==suma_odd:
        print(f"{i}", end=" ")