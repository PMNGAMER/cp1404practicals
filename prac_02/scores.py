import random

def main():
    score = float(input("Enter score: "))
    score_category = get_score_category()
    get_score_category(score)
    random_number = random.randit(1, 100)
    print(random_number)


def get_score_category(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

main()


