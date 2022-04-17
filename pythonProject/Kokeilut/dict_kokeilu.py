"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():

    my_input = ""
    my_input_splitted = ""
    my_list = []
    amount_of_a_letter = 0

    my_input = input("Enter a word: ")
    my_input_splitted = my_input.split()
    for i in range(0, len(my_input_splitted), 1):
        my_list.append(my_input_splitted[i])

    print(my_list)
    print("Sassian määrä: ")
    amount_of_a_letter = my_list.count("sassia")
    print(amount_of_a_letter)





if __name__ == "__main__":
    main()
