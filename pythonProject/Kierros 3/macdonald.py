"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def print_verse(animal_name, animal_sound):
    """Funktio tulostaa Old MacDonald -laulun, jossa parametreja
    vaihdetaan eläimen mukaan"""
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a", animal_name)
    print("E-I-E-I-O")
    print("With a", animal_sound, animal_sound, "here")
    print("And a", animal_sound, animal_sound, "there")
    print("Here a ", animal_sound, ",", " there a ", animal_sound, sep="")
    print("Everywhere a", animal_sound, animal_sound)
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")


def main():
    print_verse("cow", "moo")
    print("")
    print_verse("pig", "oink")
    print("")
    print_verse("duck", "quack")
    print("")
    print_verse("horse", "neigh")
    print("")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
