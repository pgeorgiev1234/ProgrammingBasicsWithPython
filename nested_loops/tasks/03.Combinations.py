a = int(input())

counter = 0

for x in range(0,a+1):
    for x2 in range(0, a + 1):
        for x3 in range(0, a + 1):
            if (x+x2+x3 ==a):
                counter+=1

print(counter)