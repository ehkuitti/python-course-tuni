"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Koodi tulostaa kappaletta eri parametreillä.
"""


def repeat_name(animal_name, count):
    """Toistaa eläimen nimeä"""

    if count == 1:
        print(animal_name, ", ", animal_name, " Bear", sep="")

    elif count == 3:
        print(animal_name, ", ", animal_name, " Bear", sep="")
        print(animal_name, ", ", animal_name, " Bear", sep="")
        print(animal_name, ", ", animal_name, " Bear", sep="")


def verse(clause, name):
    """Toistaa säkeistöä käyttäen mainilta tulevia parametrejä
    ja kutsuen repeat_namea eläinten nimien tulostukseen"""
    print(clause)
    print(name, ", ", name, sep="")
    print(clause)
    repeat_name(name, 3)
    print(clause)
    repeat_name(name, 1)


def main():
    verse("I know someone you don't know", "Yogi")
    print("")
    verse("Yogi has a best friend too", "Boo Boo")
    print("")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
