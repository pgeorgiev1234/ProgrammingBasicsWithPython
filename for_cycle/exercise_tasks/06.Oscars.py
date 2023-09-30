actor_name=input()
points = float(input())
judges = int(input())

for i in range (0,judges):
    judge = input()
    judge_points = float(input())
    points+=(judge_points*len(judge)/2)
    if points>1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.5-points:.1f} more!")