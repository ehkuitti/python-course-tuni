"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""

# Globaalit muuttujat
VAADITTU_MAARA_PUOLIPISTEITA_RIVILLA = 2


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
    puolipisteitä. Ottaa parametrina tiedoston yksittäisen rivin ja palauttaa
    True eli kyllä, mikäli rivillä on tarpeeksi monta puolipistettä. Muuten
    false eli ei ole."""

    puolipisteiden_maara = 0

    puolipisteiden_maara = rivi.count(";")

    return puolipisteiden_maara >= VAADITTU_MAARA_PUOLIPISTEITA_RIVILLA


def poista_rivilta_ylimaaraiset_valilyonnit(rivi):
    """Funktio poistaa riviltä kaikki ylimääräiset välilyönnit (engl.
    whitespace) ja palauttaa merkkijonon, josta ne on poistettu. Parametrina
    yksittäinen tiedoston rivi."""

    rivi_ilman_valilyonteja = ""

    rivi_ilman_valilyonteja = rivi.strip()

    return rivi_ilman_valilyonteja


def pilko_rivi_listaksi(rivi):
    rivi_listana = rivi.split(";")

    return rivi_listana


def lue_tiedosto_sanakirjaan(tiedosto):
    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPEITTÄIN AAKKOSJÄRJESTYKSESSÄ)

    # Listat
    pilkottu_rivi = []

    # Merkkijonot
    kasiteltava_rivi = ""
    kurssi = ""
    laajuus = ""
    laitos = ""

    # Sanakirjat
    opintotietokanta = {}

    # Totuusarvot
    onko_rivilla_tarpeeksi_tietoja = False

    for rivi in tiedosto:

        kasiteltava_rivi = poista_rivilta_ylimaaraiset_valilyonnit(rivi)
        onko_rivilla_tarpeeksi_tietoja = \
            onko_rivilla_tarpeeksi_puolipisteita(kasiteltava_rivi)

        if not onko_rivilla_tarpeeksi_tietoja:
            print("Error in file!")
            return

        pilkottu_rivi = pilko_rivi_listaksi(kasiteltava_rivi)

        laitos = pilkottu_rivi[0]
        kurssi = pilkottu_rivi[1]
        laajuus = pilkottu_rivi[2]

        if laitos in opintotietokanta:
            opintotietokanta[laitos][kurssi] = laajuus
        else:
            opintotietokanta[laitos] = {kurssi: laajuus}

    return opintotietokanta


def komento_tulosta_kaikki(opintotietokanta):
    print()
    for laitoksen_nimi, kurssin_tiedot in sorted(opintotietokanta.items()):
        print(f"*{laitoksen_nimi}*")
        for kurssin_nimi, opintopisteet in sorted(kurssin_tiedot.items()):
            print(f"{kurssin_nimi} : {opintopisteet} cr")


def komento_lisaa():
    pass


def main():
    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPPEITTÄIN AAKKOSJÄRJESTYKSESSÄ)

    # Merkkijonot
    komento = ""

    # Sanakirjat
    opintotietokanta = {}

    tiedosto = avaa_tiedosto()
    opintotietokanta = lue_tiedosto_sanakirjaan(tiedosto)
    if opintotietokanta is None:
        return

    print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int "
          "department / [Q]uit")
    komento = input("Enter command: ")

    if komento.upper() == "A":
        komento_lisaa()

    elif komento.upper() == "P":
        komento_tulosta_kaikki(opintotietokanta)


if __name__ == "__main__":
    main()
