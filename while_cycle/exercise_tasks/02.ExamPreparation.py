allowed_bad_grades = int(input())

bad_grades = 0
avg = 0
counter = 0
last_task  = ""

while True :
    task = input()
    if task=="Enough":
        print(f"Average score: {avg/counter:.2f}\nNumber of problems: {counter}\nLast problem: {last_task}")
        break
    grade = int(input())
    last_task = task
    if grade<=4:
        bad_grades+=1
    if bad_grades==allowed_bad_grades:
        print(f"You need a break, {allowed_bad_grades} poor grades.")
        break
    avg+=grade
    counter+=1
