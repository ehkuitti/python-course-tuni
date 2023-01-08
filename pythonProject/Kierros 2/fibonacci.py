"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():
    nterms = int(input("How many Fibonacci numbers do you want? "))
    n1 = 0
    n2 = 1
    sum = 0
    if nterms == 1:
        sum = sum + nterms
        print(sum, end=". ")
        print(n2)
    else:
        while sum < nterms:
            sum = sum + 1
            print(sum, end=". ")
            print(n2)
            nth = n1 + n2
            n1 = n2
            n2 = nth



    # lukujen_maara = 0
    # nykyinen_arvo = 1
    # edellinen_arvo = 1
    # i = 0
    #

    #
    # while i < lukujen_maara:
    #
    #     if lukujen_maara:
    #         print(nykyinen_arvo)
    #
    #     else:
    #         nykyinen_arvo -= i
    #         print(nykyinen_arvo)
    #
    #         edellinen_arvo = nykyinen_arvo
    #
    #     i += 1


if __name__ == "__main__":
    main()
