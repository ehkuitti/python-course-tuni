"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def print_box(inner_mark = " ", border_mark = "#", height = 1, width = 2):

    i = 1
    j = 1
    k = 1

    for i in range(1, height):
        for j in range(1, width):
            print(border_mark)
            while 1 < k < width - 1:
                print(inner_mark)
            k = 1
        i += 1


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
