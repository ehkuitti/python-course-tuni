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
    my_dict = {}
    amount_of_a_letter = 0

    my_input = input("Enter some words: ")

    my_input_splitted = my_input.split()
    for i in range(0, len(my_input_splitted), 1):
        my_list.append(my_input_splitted[i])

    print("My list: ", my_list)
    amount_of_a_letter = my_list.count("sassia")
    print("Amount of sassia: ", amount_of_a_letter)

    i = 0

    my_dict[my_list[i]] = amount_of_a_letter
    print(my_dict)




if __name__ == "__main__":
    main()
