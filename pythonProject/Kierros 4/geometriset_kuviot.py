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
    if float_value <= 0:
        return False
    else:
        return True


def count_values_for_a_rectangle():
    pass


def count_values_for_a_square():
    """Laskee arvoja neliölle, ei ota vastaan parametreja."""

    circumference = 0.0
    is_value_valid = False
    side_1 = 0.0
    surface_area = 0.0
    unsigned = False

    while not is_value_valid:

        side_1 = float(input("Enter the lenght of the square's side: "))
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


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            count_values_for_a_square()

        elif answer == "r":
            # Replace this comment and "pass" with your function calls dealing
            # with rectangle.
            pass

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
