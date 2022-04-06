"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Tulostaa neliön oletusarvoilla tai annetuilla parametreilla.
"""


# TODO: the definition of print_box goes here unless it goes after main.


def print_box(width=1, height=1, border_mark="#", inner_mark=' '):
    """ Jos parametrejä ei anneta, tulostaa ruudun em. oletusarvoilla."""

    # Muuttujien alustukset KÄYTTÖJÄRJESTYKSESSÄ
    rivi = 1
    sijainti_poikkeusrivilla = 1
    taydet_rivit_1_ja_vika = 1

    # Huolehtii riveistä
    for rivi in range(1, height + 1):

        # Ensimmäisen ja viimeisen rivin poikkeustapaukset, joissa tulostetaan
        # aina täysi määrä border_markkeja
        if rivi == 1 or rivi == height:

            # Täytetään rivit pelkällä border_markilla
            for taydet_rivit_1_ja_vika in range(1, width + 1):
                print(border_mark, sep="", end="")

            # Rivinvaihto for-loopin jälkeen
            print("")

        # Poikkeusrivit
        else:
            for sijainti_poikkeusrivilla in range(1, width + 1):

                # Alussa ja lopussa tulostetaan border_mark
                if sijainti_poikkeusrivilla == 1:
                    print(border_mark, sep="", end="")

                elif sijainti_poikkeusrivilla == width:
                    print(border_mark, sep="")
                # Muuten tulostetaan inner_mark
                else:
                    print(inner_mark, sep="", end="")

            sijainti_poikkeusrivilla = 1

    # Tyhjä rivi
    print("")


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
