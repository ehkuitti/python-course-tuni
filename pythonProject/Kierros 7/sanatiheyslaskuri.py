"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():

    my_input = ""
    filename = ""
    dictionary = {}
    split_my_input = []
    length_of_my_input = 0
    length_of_split_my_input = 0

    print("Enter rows of text for word counting. Empty row to quit.")

    while True:

        my_input = input()

        # Luuppi kaadetaan tyhjällä merkkijonolla, käytännössä pelkän enterin
        # syöttämisellä
        if my_input == "":
            break

        length_of_my_input = len(my_input)

        for i in range(0, length_of_my_input, 1):

            split_my_input = my_input.split()
            length_of_split_my_input = len(my_input)

            # index_1_as_int = int(split_sentence[1])

            for j in range(0, length_of_split_my_input, 1):

                if split_my_input[j] in dictionary:
                    dictionary[split_my_input[j]] = dictionary.get(
                        split_my_input[j]) + split_my_input[j].count(
                        split_my_input[j])

                else:
                    dictionary[split_my_input[j]] = split_my_input[j].count(
                        split_my_input[j])

            # print("Sanakirjan sisältö rivillä 33: ", dictionary)
    
        # print("Sortattu dictionary: ", sorted_dictionary)
    
        # sorted_dictionary = dict(sorted(dictionary.items()))
        print("Haloust world!")

        # print("Contestant score: ")
        for key, value in sorted_dictionary.items():
            print(key, value)
    

if __name__ == "__main__":
    main()

# print("Arvot splitatussa taulukossa: ", split_file_line)