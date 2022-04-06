"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def print_box(width=1, height=1, border_mark="#", inner_mark=' '):
    i = 1
    i_sisainen = 1
    j = 1
    k = 1

    for i in range(1, height + 1):

        while i_sisainen == 1 or i_sisainen == width - 1:
            print(border_mark, sep="", end="")
            i_sisainen += 1

        for j in range(1, width + 1):
            print(border_mark, sep="", end="")
            k = 1

            while k < (width - 1):
                print(inner_mark, sep="", end="")
                k += 1
            print(border_mark, sep="")

        print("")

    print("")


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
