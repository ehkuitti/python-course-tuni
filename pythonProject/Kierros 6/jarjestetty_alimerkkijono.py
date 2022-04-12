"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def longest_substring_in_order(string):

    substr = ""
    lenght_of_string = 0

    lenght_of_string = len(string)

    if lenght_of_string == 0 or lenght_of_string == 1:
        return string

    else:
        pass


def main():

    string = ""
    string = input("Input a string: ")

    longest_substring_in_order(string)


if __name__ == "__main__":
    main()
