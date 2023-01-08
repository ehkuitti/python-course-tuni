"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma korvaa taulukon alkioita arvolla nolla, mikäli
ne ovat yli nollan.
"""


def convert_grades(grades):
    """ Muuttaa listan alkioita kuutosiksi, mikäli niistä löytyy
    mitään muuta arvoa kuin nollaa. Ei tee ko. operaatiota tyhjän listan tai yhden
    alkion mittaisille listoille."""
    if len(grades) == 0:
        return

    else:
        list_lenght = len(grades)
        for index in range(0, list_lenght, 1):
            if grades[index] > 0:
                grades[index] = 6


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
