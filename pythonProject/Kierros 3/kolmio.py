"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma laskee pinta-aloja syötettyjen parametrien perusteella.
"""

from math import sqrt


def area(a, b, c):
    """Laskee pinta-aloja parametrien avulla, joiden arvot kysytään mainissa"""
    # Muuttujien alustukset
    puolet_piirista = 0
    pinta_ala = 0

    puolet_piirista = (a + b + c) / 2

    pinta_ala = sqrt(
        puolet_piirista * (puolet_piirista - a) * (puolet_piirista - b)
        * (puolet_piirista - c))

    return pinta_ala


def main():
    a = 0.0
    b = 0.0
    c = 0.0
    lopullinen_pinta_ala = 0.0

    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    lopullinen_pinta_ala = area(a, b, c)

    print(f"The triangle's area is {lopullinen_pinta_ala:.1f}")


if __name__ == "__main__":
    main()
