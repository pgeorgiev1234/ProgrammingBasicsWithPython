time_first = int(input())
time_second = int(input())
time_third = int(input())

suma = time_first + time_third + time_second
min = suma // 60
sec = suma % 60

if sec < 10:
    print(f"{min}:0{sec}")
else:
    print(f"{min}:{sec}")
