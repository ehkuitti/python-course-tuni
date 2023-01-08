"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""

def count_abbas(abbasyote):
    """Laskee meinistä tuleville abbasanoilla abbojen määrän :D."""
    abbasyotteen_pituus = ""
    abbasyotteen_pituus = len(abbasyote)
    abbain_maara = 0
    indeksi_plus_4 = 4
    i = 0
    alimerkkijono = ""

    if abbasyotteen_pituus < 4:
        return 0

    # Liikuttaa hakualuetta "abba" stringiä pitkin luoden aina uuden alimerkki-
    # jonon. Vertaa alimerkkijonoa "abba" syltteeseen, nostaa abbain määrää,
    # jos substring on "abba".
    for i in range(0, abbasyotteen_pituus, 1):
        alimerkkijono = abbasyote[i:indeksi_plus_4]
        if alimerkkijono == "abba":
            abbain_maara += 1
            indeksi_plus_4 += 1
        else:
            indeksi_plus_4 += 1

    return abbain_maara


def main():
    abbasyote = ""
    abbasyote = input("Syötä sana, josta tutkitaan abboja:")

    count_abbas(abbasyote)


if __name__ == "__main__":
    main()
