# biathlon.py

import random

def init_game():
    print("~" * 38)
    print("              Biathlon")
    print("         a hit or miss game")
    print("~" * 38)
    print("You got 5 shots\n")

def init_targets():
    return ["*"] * 5

def show_targets(targets: list):
    print("1 2 3 4 5")
    print(*targets)

def shoot(targets: list, pos: int):
    hit = random.choice([True, False])
    if hit:
        if targets[pos] == "*":
            print("Hit on open target")
            targets[pos] = "O"
        elif targets[pos] == "O":
            print("Hit on closed target")
    else:
        print("Miss")

def main():
    init_game()
    targets = init_targets()

    for i in range(1, 6):
        show_targets(targets)
        pos = int(input(f"Shot nr {i} at: ")) - 1
        shoot(targets, pos)

    hits = targets.count("O")
    print(f"You hit {hits} of 5 targets")


if __name__ == "__main__":
    main()
