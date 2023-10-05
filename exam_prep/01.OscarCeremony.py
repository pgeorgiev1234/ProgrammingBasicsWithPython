naem = int(input())

statuetki = naem - 0.3*naem
keturing = statuetki - 0.15*statuetki
sound = keturing/2
total = naem+statuetki+keturing+sound

print(f"{total:.2f}")