num1 = int(input())
num2 = int(input())
sign = input()

if sign == "+":
    even_odd = "even" if (num2 + num1) % 2 == 0 else "odd"
    print(f"{num1} + {num2} = {num2 + num1} - {even_odd}")
elif sign == "-":
    even_odd = "even" if (num1 - num2) % 2 == 0 else "odd"
    print(f"{num1} - {num2} = {num1 - num2} - {even_odd}")
elif sign == "*":
    even_odd = "even" if (num2 * num1) % 2 == 0 else "odd"
    print(f"{num1} * {num2} = {num2 * num1} - {even_odd}")
elif sign == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        print(f"{num1} / {num2} = {num1 / num2:.2f}")
elif sign == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        print(f"{num1} % {num2} = {num1 % num2}")
