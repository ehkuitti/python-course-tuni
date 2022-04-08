"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma laskee kuinka monta kappaletta tiettyä lukua löytyi.
"""


def input_to_list():
    """Änkee arvoja listaan sen edestä kun käyttäjä haluaa, palauttaa listan"""
    amount = 0
    current_number = 0
    i = 0
    my_list = []

    amount = int(input("How many numbers do you want to process: "))
    print("Enter", amount, "numbers:")

    while i < amount:
        current_number = int(input(""))
        my_list.append(current_number)
        i += 1

    return my_list


def main():

    amount_of_numbers = 0
    lista_main = []
    number_to_be_serched = 0

    lista_main = input_to_list()

    number_to_be_serched = int(input("Enter the number to be searched: "))

    amount_of_numbers = lista_main.count(number_to_be_serched)
    if amount_of_numbers <= 0:
        print(number_to_be_serched, "is not among the numbers "
                                    "you have entered.")
    else:
        print(number_to_be_serched, "shows up"
              , amount_of_numbers, "times among the numbers you have entered.")


if __name__ == "__main__":
    main()
