"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def longest_substring_in_order(merkkijono):
    """Käy muuttujat läpi aakkosjärjestyksessä, palauttaa substringin."""
    # Muuttujat aakkojärjestyksessä
    alimerkkijono = ""
    merkkijonon_pituus = len(merkkijono)
    englannin_aakkoset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                          "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                          "u", "v", "w", "x", "y", "z"]
    englannin_aakkosten_indeksi = 0
    englannin_aakkosten_pituus = len(englannin_aakkoset)

    if merkkijonon_pituus == 0 or merkkijonon_pituus == 1:
        return merkkijono

    for i in range(0, merkkijonon_pituus, 1):
        if i > englannin_aakkosten_pituus:
            englannin_aakkosten_indeksi = 0
        elif merkkijono[i] >= englannin_aakkoset[englannin_aakkosten_indeksi]:
            alimerkkijono += merkkijono[i]
            englannin_aakkosten_indeksi += 1

    return alimerkkijono


def main():
    string = ""
    string = input("Input a string: ")

    longest_substring_in_order(string)


if __name__ == "__main__":
    main()
