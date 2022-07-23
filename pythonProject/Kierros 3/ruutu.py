"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma tulostaa ruudun käyttäjän antamien mittojen ja merkin mukaisesti
"""


def print_box(leveys, korkeus, merkki):
    """ Tämän funktion tarkoituksena on tulostaa ruudukko, joka
    saa kokonsa ja merkkinsä mainista parametreinä."""
    for i in range(0, korkeus):
        print(leveys * merkki, sep="", end="")
        print("")


def main():
    leveys = int(input("Enter the width of a frame: "))
    korkeus = int(input("Enter the height of a frame: "))
    merkki = input("Enter a print mark: ")
    print("")
    print_box(leveys, korkeus, merkki)


if __name__ == "__main__":
    main()
