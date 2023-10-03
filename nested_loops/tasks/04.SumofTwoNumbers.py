border1=int(input())
border2=int(input())
magic_num=int(input())

counter = 0
isFound=False

for i in range(border1,border2+1):
    for j in range (border1,border2+1):
        counter+=1
        if i + j ==magic_num:
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            isFound=True
            break
    if isFound:
        break
if not isFound:
    print(f"{counter} combinations - neither equals {magic_num}")