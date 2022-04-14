"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def longest_substring_in_order(merkkijono):
    """Käy muuttujat läpi aakkosjärjestyksessä, palauttaa substringin."""
    # Muuttujat aakkosjärjestyksessä
    alimerkkijono = ""
    alimerkkijonon_pituus = 0
    indeksi = 0
    merkkijonon_pituus = len(merkkijono)
    pisin_alimerkkijono = ""
    pisin_alimerkkijonon_pituus = 0

    if merkkijonon_pituus == 0 or merkkijonon_pituus == 1:
        return merkkijono

    for i in range(0, merkkijonon_pituus, 1):

        # TÄMÄ TEHDÄÄN VAIN EKALLA KIERROKSELLA, MUTTA SILLOIN AINA
        if i == 0:
            alimerkkijono += merkkijono[0]
            alimerkkijonon_pituus = 1

        # JOS KIRJAIN ON SAMA KUIN EDELLINEN
        elif merkkijono[i] == merkkijono[i-1]:
            alimerkkijono = merkkijono[i]
            alimerkkijonon_pituus = 1

        # JOS KIRJAIN AAKKOSISSA MYÖHÄISEMPI KUIN EDELLINEN
        elif merkkijono[i] > merkkijono[i-1]:
            alimerkkijono += merkkijono[i]
            alimerkkijonon_pituus += 1

        if alimerkkijonon_pituus > pisin_alimerkkijonon_pituus:
            pisin_alimerkkijono = alimerkkijono
            pisin_alimerkkijonon_pituus = alimerkkijonon_pituus

        else:
            alimerkkijono = merkkijono[i]
            alimerkkijonon_pituus = 1

    return pisin_alimerkkijono


def main():
    string = ""
    string = input("Input a string: ")

    longest_substring_in_order(string)


if __name__ == "__main__":
    main()
