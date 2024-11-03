import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    quick_picks = int(input("How many quick picks? "))

    for _ in range(quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in sorted(quick_pick)))


def generate_quick_pick():
    """Generates a quick pick (a set of 6 random unique numbers)."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    return quick_pick


main()
