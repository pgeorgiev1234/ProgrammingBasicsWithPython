while(True):
    destiantion = input()
    if destiantion=="End":
        break
    budget = float(input())
    suma = 0
    while True:
        money = float(input())
        suma+=money
        if suma>=budget:
            print(f"Going to {destiantion}!")
            break