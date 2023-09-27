budget = float(input())
videocards = int(input())
processor = int(input())
ramcards = int(input())

videocards_price = videocards*250
processor_price = (videocards_price*0.35)*processor
ramcards_price = (0.1*videocards_price)*ramcards
total = videocards_price+processor_price+ramcards_price
total = 0.85*total if videocards>processor else total

if total<=budget:
    print(f"You have {budget-total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total-budget:.2f} leva more!")
