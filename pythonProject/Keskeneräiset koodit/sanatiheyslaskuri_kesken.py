"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def count_amount_of_a_word():
    """Funktion tarkoituskena on tallentaa sanoja taulukkoon ja laskea niiden
    määriä."""
    amount_of_found_words = 0
    lenght_of_my_split_input = ""
    my_input = ""
    my_list = []
    my_lowercase_input = ""
    my_split_input = ""
    my_dict = {}
    is_input_valid = True
    word_i_count = 0

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
        i_value_in_memory = 0

        for i in range(0, lenght_of_my_split_input, 1):
            # Lisää arvoja taulukkoon
            my_list.append(my_split_input[i])
            # print("My list in for loop: ", my_list)

        i = 0
        while i < lenght_of_my_split_input:
            word_i_count = my_list.count(my_split_input[i])
            # print("My i word count: ", word_i_count)
            i += 1

        my_dict[my_split_input[i - 1]] = word_i_count

    print("My dict: ", my_dict)
    print("My list: ", my_list)
    # print("Sassia count: ", my_list.count("sassia"))


def main():
    count_amount_of_a_word()


"""
if __name__ == "__main__":
    main()

length_of_my_input = len(my_input)

for j in range(0, length_of_my_input, 1):

    split_my_input = my_input.split()
    length_of_split_my_input = len(my_input)

    # index_1_as_int = int(split_sentence[1])

    for j in range(0, length_of_split_my_input, 1):

        if split_my_input[j] == split_my_input[-1]:
            is_word_traversion_over = True

        if split_my_input[j] in dictionary:
            dictionary[split_my_input[j]] = dictionary.get(
                split_my_input[j]) + split_my_input[j].count(
                split_my_input[j])

        else:
            dictionary[split_my_input[j]] = split_my_input[j].count(
                split_my_input[j])

        if is_word_traversion_over:
            break

    break

"""
