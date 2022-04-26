"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""

# Globaalit muuttujat
VAADITTU_MAARA_PUOLIPISTEITA_RIVILLA = 2
LOPETUSKOMENTO = "q"


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


def pilko_listaksi(syote, erotinmerkki=" "):
    listana = syote.split(erotinmerkki)

    return listana


def lue_tiedosto_sanakirjaan(tiedosto):
    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPEITTÄIN AAKKOSJÄRJESTYKSESSÄ)

    # Listat
    pilkottu_rivi = []

    # Merkkijonot
    erotinmerkki = ";"
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

        pilkottu_rivi = pilko_listaksi(kasiteltava_rivi, erotinmerkki)

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


def komento_tulosta_laitos(komento, opintotietokanta):
    """"""

    # MUUTTUJIEN ALUSTUKSET (TYYPEITTÄIN AAKKOSJÄRJESTYKSESSÄ)

    # Listat
    pilkottu_komento = []

    # Merkkijonot
    komento_merkki = ""
    komento_laitos = ""

    pilkottu_komento = pilko_listaksi(komento)

    komento_merkki = pilkottu_komento[0]
    komento_laitos = pilkottu_komento[1]

    if komento_laitos not in opintotietokanta:
        print("Department not found!")
        return

    print()
    for laitoksen_nimi, kurssin_tiedot in sorted(opintotietokanta.items()):
        if laitoksen_nimi == komento_laitos:
            print(f"*{laitoksen_nimi}*")
            for kurssin_nimi, opintopisteet in sorted(kurssin_tiedot.items()):
                print(f"{kurssin_nimi} : {opintopisteet} cr")


def komento_tulosta_opintopisteiden_maara(komento, opintotietokanta):
    pilkottu_komento = pilko_listaksi(komento)

    opintopisteiden_kokonaismaara = 0

    komento_merkki = pilkottu_komento[0]
    komento_laitos = pilkottu_komento[1]

    if komento_laitos not in opintotietokanta:
        print("Department not found!")
        return

    for laitoksen_nimi, kurssin_tiedot in sorted(opintotietokanta.items()):
        if laitoksen_nimi == komento_laitos:
            for kurssin_nimi, opintopisteet in sorted(kurssin_tiedot.items()):
                opintopisteiden_kokonaismaara += int(opintopisteet)

    print(f"Department {komento_laitos} has to offer "
          f"{opintopisteiden_kokonaismaara} cr.")


def komento_lisaa_kurssi(komento, opintotietokanta):



def main():
    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPPEITTÄIN AAKKOSJÄRJESTYKSESSÄ)

    # Merkkijonot
    komento = ""

    # Sanakirjat
    opintotietokanta = {}

    # Totuusarvot
    onko_syotetty_lopetuskomento = False

    tiedosto = avaa_tiedosto()
    opintotietokanta = lue_tiedosto_sanakirjaan(tiedosto)
    if opintotietokanta is None:
        return

    while not onko_syotetty_lopetuskomento:
        print()
        print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int "
              "department / [Q]uit")
        komento = input("Enter command: ")

        if komento.lower() == "a":
            komento_lisaa()

        elif komento.lower() == "p":
            komento_tulosta_kaikki(opintotietokanta)

        elif komento.find("c") != -1:
            komento_tulosta_opintopisteiden_maara(komento, opintotietokanta)

        elif komento.find("r") != -1:
            komento_tulosta_laitos(komento, opintotietokanta)

        elif komento.lower() == LOPETUSKOMENTO:
            print("Ending program!")
            return

        else:
            print("Invalid command!")
            print()


if __name__ == "__main__":
    main()
