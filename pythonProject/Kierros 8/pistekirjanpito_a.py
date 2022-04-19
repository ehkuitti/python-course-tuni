"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():

    filename = ""

    filename = input("Enter the name of the score file: ")

    try:
        file = open(filename, mode="r")

        for file_line in file:

            # Poistaa tyhjät rivit tiedostosta (row strip)
            file_line = file_line.rstrip()

    except OSError:
        print("Error opening file!")


if __name__ == "__main__":
    main()
