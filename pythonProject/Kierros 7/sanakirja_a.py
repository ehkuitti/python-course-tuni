"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)

    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    input_word = ""
    word_in_english = ""
    word_in_spanish = ""

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            input_word = input("Enter the input_word to be translated: ")

            if input_word in english_spanish:
                print(input_word, "in Spanish is", english_spanish[input_word])

            else:
                print("The input_word", input_word,
                      "could not be found from the dictionary.")

        elif command == "A":
            word_in_english = \
                input("Give the input_word to be added in English: ")
            word_in_spanish = \
                input("Give the input_word to be added in Spanish: ")

            if word_in_spanish not in english_spanish:
                english_spanish[word_in_english] = word_in_spanish

        elif command == "R":
            input("Give the input_word to be removed: ")

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
