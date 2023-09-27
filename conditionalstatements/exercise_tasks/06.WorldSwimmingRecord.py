import math

current_record = float(input())
meters = float(input())
secs_per_meter= float(input())

slowing_down = math.floor(meters/15) * 12.5
time = meters*secs_per_meter + slowing_down

if time>=current_record:
    print(f"No, he failed! He was {time-current_record:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
