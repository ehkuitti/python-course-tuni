"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma laskee pinta-aloja erilaisille kuvioille käyttäjän syötteen perusteella.
"""

from math import pi
from math import pow


def is_value_unsigned(float_value):
    """Funktio tarkistaa, onko parametrinä
    annettu liukuluku positiivinen (unsigned)"""
    if float_value <= 0:
        return False
    else:
        return True


def count_values_for_a_rectangle():
    """Funktio tulostaa pinta-alan ja piirin suorakaiteelle."""
    side_1 = 0.0
    side_2 = 0.0

    circumference = 0.0
    is_inner_value_valid = False
    is_value_valid = False
    side_1 = 0.0
    side_2 = 0.0
    surface_area = 0.0
    unsigned = False

    while not is_value_valid:

        side_1 = float(input("Enter the length of the rectangle's side 1: "))
        unsigned = is_value_unsigned(side_1)
        if not unsigned:
            continue

        else:
            while not is_inner_value_valid:
                side_2 = float(input("Enter the length of the rectangle's side 2: "))
                unsigned = is_value_unsigned(side_2)
                if not unsigned:
                    continue
                else:
                    is_inner_value_valid = True

            is_value_valid = True

    circumference = (2 * side_1) + (2 * side_2)
    print(f"The circumference is {circumference:.2f}")
    surface_area = side_1 * side_2

    print(f"The surface area is {surface_area:.2f}")

    return


def incorrect_entry():
    """Funktio tulostaa virheilmoituksen
    väärästä syötteestä."""
    print("Incorrect entry, try again!")


def count_values_for_a_square():
    """Laskee arvoja neliölle, ei ota vastaan parametreja."""

    circumference = 0.0
    is_value_valid = False
    side_1 = 0.0
    surface_area = 0.0
    unsigned = False

    while not is_value_valid:

        side_1 = float(input("Enter the length of the square's side: "))
        unsigned = is_value_unsigned(side_1)
        if not unsigned:
            continue
        else:
            circumference = 4 * side_1
            print(f"The circumference is {circumference:.2f}")

            surface_area = pow(side_1, 2)
            print(f"The surface area is {surface_area:.2f}")
            is_value_valid = True

    return


def quit_program():
    """Funktio sammuttaa ohjelman kokonaan palauttamalla nollan
    eli arvon >>sammutus onnistui>>"""
    return 0


def count_values_for_a_circle():
    """Laskee arvoja neliölle, ei ota vastaan parametreja."""

    circumference = 0.0
    is_value_valid = False
    side_1 = 0.0
    surface_area = 0.0
    unsigned = False

    while not is_value_valid:

        side_1 = float(input("Enter the circle's radius: "))
        unsigned = is_value_unsigned(side_1)
        if not unsigned:
            continue
        else:
            circumference = 2 * pi * side_1
            print(f"The circumference is {circumference:.2f}")

            surface_area = pi * (pow(side_1, 2))
            print(f"The surface area is {surface_area:.2f}")
            is_value_valid = True

    return


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            count_values_for_a_square()

        elif answer == "r":
            count_values_for_a_rectangle()

        elif answer == "c":
            count_values_for_a_circle()

        elif answer == "q":
            quit_program()
            return

        else:
            incorrect_entry()

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
