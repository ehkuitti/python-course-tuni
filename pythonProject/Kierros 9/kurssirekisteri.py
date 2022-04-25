"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def avaa_tiedosto():
    """Funktio kysyy käyttäjältä tiedostonimeä ja yrittää avata sen nimistä
    tiedostoa samasta kansiosta, jossa tämä tiedosto sijaitsee. Avauksen
    epäonnistuessa tulostetaan virhe ja ohjelma sammutetaan. Funktio ei ota
    parametrejä vastaan ja palauttaa tiedosto-olion."""

    tiedostonimi = ""

    tiedostonimi = input("Enter file name: ")

    try:
        tiedosto = open(tiedostonimi, mode="r")

    except OSError:
        print("Error opening file!")
        return

    return tiedosto


def lue_tiedosto_tietorakenteeseen(tiedosto):

    puolipisteiden_maara = 0
    rivi_stripattuna = ""

    for rivi in tiedosto:
        rivi_stripattuna = rivi.strip()
        puolipisteiden_maara = rivi_stripattuna.count(";")
        if puolipisteiden_maara < 2:
            print("Error in file!")
            return

    return tiedosto


def main():

    tiedosto = avaa_tiedosto()
    tietorakenne = lue_tiedosto_tietorakenteeseen(tiedosto)


if __name__ == "__main__":
    main()
