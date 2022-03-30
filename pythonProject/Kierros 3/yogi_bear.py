"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Koodi tulostaa kappaletta eri parametreillä.
"""


def repeat_name(animal_name, count = 0):
    """Toistaa eläimen nimeä"""
    print(animal_name, ", ", animal_name, sep="", end="")


def verse(clause, name):
    """Toistaa säkeistöä käyttäen mainilta tulevia parametrejä
    ja kutsuen repeat_namea eläinten nimien tulostukseen"""
    print(clause)
    repeat_name(name)
    print("\n", clause, sep="")
    repeat_name(name)
    print(" Bear")
    repeat_name(name)
    print(" Bear")
    repeat_name(name)
    print(" Bear")
    print(clause)
    repeat_name(name)
    if name == "Cindy":
        print(" Bear", end="")
    else:
        print(" Bear", "\n", sep="")


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
