"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""


def read_input(lause):
    """Funktio lukee käyttäjältä syötettä, palauttaa mainille arvoja"""

     = False

    while not :

        str_arvo = input(lause) # Ottaa arvon stringinä vastaan
        arvo = int(str_arvo) # Converttaa arvon intiksi

        if arvo <= 0:
            continue
        else:
             = True

    return arvo


def print_box(leveys, korkeus, merkki):
    """ Tämän funktion tarkoituksena on tulostaa ruudukko, joka
    saa kokonsa ja merkkinsä mainista parametreinä."""
    for i in range(0, korkeus):
        print(leveys * merkki, sep="", end="")
        print("")
        i += 1


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print("")
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
