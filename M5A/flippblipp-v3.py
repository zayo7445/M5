# flippblipp-v3.py

def flippblipp(n):
    if n % 3 == 0 and n % 5 == 0:
        return "flipp blipp"
    elif n % 5 == 0:
        return "blipp"
    elif n % 3 == 0:
        return "flipp"
    else:
        return str(n)

run = True
current = 1
print(current)

while run:
    current += 1
    n = input("Nästa: ")
    ans = flippblipp(current)
    if n != ans:
        print(f"Fel - {ans}")
        print("Game over")
        run = False
