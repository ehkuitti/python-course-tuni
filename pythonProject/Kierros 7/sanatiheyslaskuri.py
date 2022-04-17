"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():

    input_dictionary = {}

    my_input = input("Enter rows of text for word counting. Empty row to quit.")

    lowercase_input = my_input.lower()
    split_lowecase_input = lowercase_input.split()

    while my_input != "":
        my_input = input()


if __name__ == "__main__":
    main()
