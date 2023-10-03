name = input()

current_class=1
grade =0
fails = 0


while current_class<=12:
    ocenka = float(input())
    if ocenka>=4:
        current_class+=1
        grade+=ocenka
        continue
    else:
        fails+=1

    if fails>=2:
        print(f"{name} has been excluded at {current_class} grade")
        break

if fails <2:
    print(f"{name} graduated. Average grade: {grade/12:.2f}")