steps = 0

while True:
    command = input()
    if command =="Going home":
        step = int(input())
        steps+=step
        if steps<10000:
            print(f"{10000-steps} more steps to reach goal.")
            break
        else:
            print(f"Goal reached! Good job!\n{steps-10000} steps over the goal!")
            break
    step=int(command)
    steps +=step
    if steps>=10000:
        print(f"Goal reached! Good job!\n{steps - 10000} steps over the goal!")
        break