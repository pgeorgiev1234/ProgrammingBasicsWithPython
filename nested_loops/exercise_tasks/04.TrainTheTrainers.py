import math

n = int(input())

sum_all=0
counter = 0

while True:
    test = input()
    if test =="Finish":
        print(f"Student's final assessment is {sum_all/counter:.2f}.")
        break
    suma = 0
    for i in range(0,n):
        grade = float(input())
        suma+=grade
    sum_all+=suma
    counter+=n
    print(f"{test} - {suma/n:.2f}.")