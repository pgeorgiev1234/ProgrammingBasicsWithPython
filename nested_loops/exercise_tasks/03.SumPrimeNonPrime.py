sum_prime=0
sum_nonprime=0

while True:
    number=input()
    if number=="stop":
        break
    number1=int(number)
    is_prime=True

    if number1<0:
        print("Number is negative.")
        continue

    for i in range(2,number1):
        if number1%i==0:
            is_prime=False
            break
    if is_prime:
        sum_prime+=number1
    else:
        sum_nonprime+=number1


print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_nonprime}")
