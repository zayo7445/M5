# biathlon.py

import random


def init_game():
    print("~" * 38)
    print("              Biathlon")
    print("         a hit or miss game")
    print("~" * 38)
    print("You got 5 shots")


def init_targets():
    return ["*"] * 5


def show_targets(targets: list):
    print("\n1 2 3 4 5")
    print(*targets)


def shoot(targets: list, pos: int):
    if targets[pos] == "O":
        print("Hit on closed target")
        return
    hit = random.choice([True, False])
    if hit:
        print("Hit on open target")
        targets[pos] = "O"
    else:
        print("Miss")


def get_input(i: int):
    while True:
        pos = input(f"Shot nr {i} at: ")
        if pos.isdigit():
            pos = int(pos)
            if 1 <= pos <= 5:
                return pos - 1
        print("Invalid input. Try again.\n")


def main():
    init_game()
    targets = init_targets()

    for i in range(1, 6):
        show_targets(targets)
        pos = get_input(i)
        shoot(targets, pos)

    show_targets(targets)
    hits = targets.count("O")
    print(f"You hit {hits} of 5 targets")


if __name__ == "__main__":
    main()
