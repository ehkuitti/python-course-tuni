"""This program checks the user input for a letter. This letter is then used
to control the condition of the while loop. The loop ends with a positive
affirmation. """


def main():

    answer = "n"

    while answer != "y":
        answer = input("Bored? (y/n) ")

    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()
