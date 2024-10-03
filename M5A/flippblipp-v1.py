# flippblipp-v1.py

n = 40

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("flipp blipp")
    elif i % 5 == 0:
        print("blipp")
    elif i % 3 == 0:
        print("flipp")
    else:
        print(i)
