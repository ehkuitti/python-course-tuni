"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():

    while True:
        inputti = input("Bored? (y/n) ")
        if inputti == "y":
            print("Well, let's stop this, then.")
            break
        if inputti != "n":
            print("Incorrect entry.")


if __name__ == "__main__":
    main()