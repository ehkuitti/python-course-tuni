"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma vertailee liukulukuja käyttämällä EPSILONia, joka on itseis-
arvoltaan todella pieni.
"""

from math import e

EPSILON = 0.000000001


def compare_floats(a, b, epsilon = 0.000000001):
    """Tämä funktio vertaa, onko arvojen välinen erotus
    epsilonin verran (hyvin hyvin pieni) vaiko ei."""
    return abs(a) - abs(b) < epsilon


def main():
    pass

    a = float(input("Input first number: "))
    b = float(input("Input second number: "))

    print(compare_floats(a, b, EPSILON))


if __name__ == "__main__":
    main()
