degrees = int(input())
time = input()

outfit = None
shoes = None

if 10<=degrees<=18:
    if time=="Morning":
        outfit="Sweatshirt"
        shoes="Sneakers"
    elif time == "Afternoon":
        outfit="Shirt"
        shoes="Moccasins"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18<=degrees<=24:
    if time == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time == "Afternoon":
       outfit="T-Shirt"
       shoes="Sandals"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"
else:
    if time == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time == "Afternoon":
        outfit="Swim Suit"
        shoes="Barefoot"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
