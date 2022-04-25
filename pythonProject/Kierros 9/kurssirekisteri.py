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


def onko_rivilla_tarpeeksi_puolipisteita(rivi):
    """Funktio tarkistaa, onko annetulla tiedostorivillä tarpeeksi
    puolipisteitä. Palauttaa True eli \"kyllä\", mikäli rivillä on tarpeeksi
    monta puolipistettä. Muuten false eli \"ei\"."""

    puolipisteiden_maara = 0

    puolipisteiden_maara = rivi.count(";")

    return puolipisteiden_maara >= 2


def poista_rivilta_ylimaaraiset_valilyonnit(rivi):

    valilyonniton_rivi = ""

    valilyonniton_rivi = rivi.strip()

    return valilyonniton_rivi


def lue_tiedosto_tietorakenteeseen(tiedosto):

    valilyonniton_rivi = ""
    onko_rivi_tarpeeksi_pitka = False

    for rivi in tiedosto:
        valilyonniton_rivi = poista_rivilta_ylimaaraiset_valilyonnit(rivi)
        onko_rivi_tarpeeksi_pitka = onko_rivilla_tarpeeksi_puolipisteita(rivi)
        if onko_rivi_tarpeeksi_pitka:
            print("Error in file!")
            return

    return tiedosto


def main():

    tiedosto = avaa_tiedosto()
    tietorakenne = lue_tiedosto_tietorakenteeseen(tiedosto)


if __name__ == "__main__":
    main()
