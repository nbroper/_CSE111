
positive = 1
negative = -1

def main():

    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    score = 0
    score += question("1. I feel that I am a person of worth, at least on an"
        "equal plane with others.", positive)
    score += question("2. I feel that I have a number of good qualities.", positive)
    score += question("3. All in all, I am inclined to feel that I am a failure.", negative)
    score += question("4. I am able to do things as well as most other people.", positive)
    score += question("5. I feel I do not have much to be proud of.", negative)
    score += question("6. I take a positive attitude toward myself.", positive)
    score += question("7. On the whole, I am satisfied with myself.", positive)
    score += question("8. I wish I could have more respect for myself.", negative)
    score += question("9. I certainly feel useless at times.", negative)
    score += question("10. At times I think I am no good at all.", negative)

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def question(statement, pos_or_negative):

    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3

    if pos_or_negative == negative:
        score = 3 - score

    return score


if __name__ == "__main__":
    main()