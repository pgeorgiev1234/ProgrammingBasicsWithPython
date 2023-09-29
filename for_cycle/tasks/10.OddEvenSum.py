n = int(input())
sum_odd=0
sum_even=0

for i in range (0,n):
    a=int(input())
    if i%2==0:
        sum_even+=a
    else:
        sum_odd+=a

if sum_even==sum_odd:
    print(f"Yes\nSum = {sum_odd}")
else:
    print(f"No\nDiff = {abs(sum_odd-sum_even)}")