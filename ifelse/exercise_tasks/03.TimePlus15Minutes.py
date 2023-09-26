hours = int(input())
minutes = int(input())

minutes +=15

if minutes <60 :
    print(f"{hours}:{minutes}")
else:
    hours +=1
    minutes -=60
    minutes ="0"+str(minutes) if minutes<10 else minutes
    hours = 0 if hours==24 else hours
    print(f"{hours}:{minutes}")

