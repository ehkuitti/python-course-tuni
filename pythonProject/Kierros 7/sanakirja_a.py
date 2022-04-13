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
    sorted_english_spanish = {}
    word_in_english = ""
    word_in_spanish = ""
    word_to_be_removed = ""


    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            input_word = input("Enter the word to be translated: ")

            if input_word in english_spanish:
                print(input_word, "in Spanish is", english_spanish[input_word])

            else:
                print("The word", input_word,
                      "could not be found from the dictionary.")

        elif command == "A":
            word_in_english = \
                input("Give the word to be added in English: ")
            word_in_spanish = \
                input("Give the word to be added in Spanish: ")

            if word_in_spanish not in english_spanish:
                english_spanish[word_in_english] = word_in_spanish

        elif command == "R":
            word_to_be_removed = input("Give the word to be removed: ")

            if word_to_be_removed in english_spanish:
                del english_spanish[word_to_be_removed]
            else:
                print("The word hey could not be found from the dictionary.")

        elif command == "P":

            # TÄRKEÄÄÄÄÄÄ!!!!!!!!! Tulostaa aakkosjärjestyksessä arvot avaimen
            # mukaan
            for avain in sorted(english_spanish):
                print(avain, english_spanish[avain])

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
