money_needed = float(input())
money = float(input())

days = 0
days_spending=0

while True:
    action = input()
    ammount = float(input())

    if action=="spend":
        days+=1
        days_spending+=1
        money -=ammount
        if money<0:
            money=0
    else:
        days+=1
        days_spending=0
        money+=ammount

    if money>=money_needed:
        print(f"You saved the money for {days} days.")
        break

    if days_spending==5:
        print(f"You can't save the money.\n{days}")
        break