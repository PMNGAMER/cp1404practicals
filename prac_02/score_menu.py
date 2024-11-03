def main():
    score = get_valid_score()
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)

    choice = input("Choose an option: ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_result(score)
            print(f"Your result is: {result}")
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid choice")

        print(menu)
        choice = input("Choose an option: ").upper()

    print("Goodbye!")


def get_valid_score():
    score = int(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Please enter a score between 0 and 100.")
        score = int(input("Enter a valid score (0-100): "))
    return score


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * score)


main()
