"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():

    file_line = ""
    filename = ""
    dictionary = {}
    split_file_line = []

    filename = input("Enter the name of the score file: ")

    try:
        file = open(filename, mode="r")

        for file_line in file:

            split_file_line = file_line.split()
            lenght_of_split_file_line = len(split_file_line)
            if lenght_of_split_file_line < 2:
                print("There was an erroneous line in the file:")
                print(file_line, end="")
                return

            index_1_as_int = int(split_file_line[1])

            if split_file_line[0] in dictionary:
                dictionary[split_file_line[0]] = dictionary.get(
                    split_file_line[0]) + index_1_as_int
            else:
                dictionary[split_file_line[0]] = index_1_as_int

            # print("Sanakirjan sisältö rivillä 33: ", dictionary)

        # print("Sortattu dictionary: ", sorted_dictionary)

        sorted_dictionary = dict(sorted(dictionary.items()))

        print("Contestant score: ")
        for key, value in sorted_dictionary.items():
            print(key, value)

    except OSError:
        print("There was an error in reading the file.")

    except ValueError:
        print("There was an erroneous score in the file:")
        print(split_file_line[1])


if __name__ == "__main__":
    main()

# print("Arvot splitatussa taulukossa: ", split_file_line)