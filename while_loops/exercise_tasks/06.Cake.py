length = int(input())
width = int(input())

size = length*width
suma = 0

while True:
    vhod = input()
    if vhod=="STOP":
        print(f"{size-suma} pieces are left.")
        break
    suma += int(vhod)
    if suma >size:
        print(f"No more cake left! You need {suma-size} pieces more.")
        break
