price_journey = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

ammount = puzzles +dolls+bears+minions+trucks >=50
total = puzzles*2.6 + dolls*3 + bears*4.1 + minions*8.2 + trucks*2
total = total*0.75 if ammount else total
total = 0.9*total

if total >=price_journey:
    print(f"Yes! {total-price_journey:.2f} lv left.")
else:
    print(f"Not enough money! {price_journey-total:.2f} lv needed.")
