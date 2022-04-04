"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""

from math import factorial


def laske_todennakoisyys(palloja_yhteensa, nostettavat_pallot):
    """Laskee todennäköisyyden lotolle parametrien perusteella. """

    # print("Palloja yhteensä: ", palloja_yhteensa)
    # print("Nostettavat pallot: ", nostettavat_pallot)
    #

    kertoma = 0

    kertoma = factorial(palloja_yhteensa) / \
              (factorial(palloja_yhteensa - nostettavat_pallot) * factorial(nostettavat_pallot))

    print(f"The probability of guessing all {nostettavat_pallot} balls correctly is 1/{kertoma:.0f}", sep="")

    return


def kysy_tiedot(palloja_yhteensa, nostettavat_pallot):
    """Kysyy tietoja, joille käyttäjä
    haluaa laskea lottotodennäköisyyden."""

    while True:
        palloja_yhteensa = int(input("Enter the total number of lottery balls: "))
        nostettavat_pallot = int(input("Enter the number of the drawn balls: "))
        if nostettavat_pallot <= 0 or palloja_yhteensa <= 0:
            print("The number of balls must be a positive number.")
            return
        if nostettavat_pallot > palloja_yhteensa:
            print("At most the total number of balls can be drawn.")
            return
        else:
            laske_todennakoisyys(palloja_yhteensa, nostettavat_pallot)
            return

    return


def main():
    nostettavat_pallot = 0
    palloja_yhteensa = 0

    kysy_tiedot(nostettavat_pallot, palloja_yhteensa)

    return


if __name__ == "__main__":
    main()
