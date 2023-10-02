width = int(input())
height = int(input())
lenght = int(input())

size = width*height*lenght

while True :
    vhod = input()
    if vhod=="Done":
        print(f"{size} Cubic meters left.")
        break
    size-=int(vhod)
    if size<0:
        print(f"No more free space! You need {abs(size)} Cubic meters more.")
        break