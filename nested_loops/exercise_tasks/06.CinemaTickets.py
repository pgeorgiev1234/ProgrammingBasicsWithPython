total_tickets = 0
students_tickets = 0
kids_tickets = 0
standart_tickets = 0

while True:
    film = input()
    if film == "Finish":
        print(f"Total tickets: {total_tickets}")
        print(f"{students_tickets / total_tickets * 100:.2f}% student tickets.")
        print(f"{standart_tickets / total_tickets * 100:.2f}% standard tickets.")
        print(f"{kids_tickets / total_tickets * 100:.2f}% kids tickets.")
        break
    free_space = int(input())
    tickets = 0
    for i in range(free_space):
        ticket = input()
        if ticket == "End":
            break
        if ticket == "standard":
            standart_tickets += 1
        elif ticket == "kid":
            kids_tickets += 1
        else:
            students_tickets += 1
        tickets += 1
    total_tickets += tickets
    print(f"{film} - {tickets / free_space * 100:.2f}% full.")
