import math

name_series = input()
episode_length = int(input())
break_length = int(input())

lunch = break_length/8
chill_time = break_length/4
break_length-=lunch+chill_time

if break_length>=episode_length:
    print(f"You have enough time to watch {name_series} and left with {math.ceil(break_length-episode_length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {math.ceil(episode_length-break_length)} more minutes")
