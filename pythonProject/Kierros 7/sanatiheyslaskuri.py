"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def count_amount_of_a_word():

    lenght_of_my_split_input = ""
    my_input = ""
    my_lowercase_input = ""
    my_split_input = ""
    my_dict = {}
    is_input_valid = True

    print("Enter rows of text for word counting. Empty row to quit.")

    # Syötteen keräämistä jatketaan niin kauan, kunnes syötetään pelkkä enter
    while is_input_valid:

        my_input = input()

        if my_input == "":
            is_input_valid = False

        else:
            my_lowercase_input = my_input.lower()
            my_split_input \
                = my_lowercase_input.split()

        lenght_of_my_split_input = len(my_split_input)

        for i in range(0, lenght_of_my_split_input, 1):

            # Jos tiettyä sanaa ei löydy sanakirjasta, se lisätään sinne
            # avaimeksi. Sen arvoksi annetaan määrä, joka on indeksi + 1 (
            # indeksointi alkaa nollasta, positiivinen määrä ei).
            if my_split_input[i] not in my_dict:
                my_dict[my_split_input[i]] = i+1

            # elif my_split_input[i] in my_dict:


    print(my_dict)

def main():

    count_amount_of_a_word()


if __name__ == "__main__":
    main()
