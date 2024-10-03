# flippblipp-v2.py

def flippblipp(n):
    if n % 3 == 0 and n % 5 == 0:
        return "flipp blipp"
    elif n % 5 == 0:
        return "blipp"
    elif n % 3 == 0:
        return "flipp"
    else:
        return str(n)

res = flippblipp(1)
print(res)
