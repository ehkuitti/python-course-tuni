"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def onko_arvo_pariton(arvo):
    return arvo % 2 > 0


def laske_mediaani(paivat, paivien_maara):
    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    keskimmaisten_keskiarvo = 0
    mediaani = 0
    parillinen_keskimmainen_arvo_1 = 0
    parillinen_keskimmainen_arvo_2 = 0
    pariton_keskimmainen_arvo = 0

    # Taulukko järjestetään pienimmästä suurimpaan mediaanin selvittämiseksi
    paivat.sort()

    # Pariton määrä arvoja
    if onko_arvo_pariton(paivien_maara):

        # Keskimmainen sijaitsee taulukon puolivälissä
        pariton_keskimmainen_arvo = (paivien_maara // 2)
        mediaani = paivat[pariton_keskimmainen_arvo]

    # Parillinen määrä arvoja
    else:

        # Otetaan muuttujiin talteen kaksi keskimmäistä arvoa sekä niiden
        # keskiarvo
        pariton_keskimmainen_arvo_1 = (paivien_maara // 2) - 1
        pariton_keskimmainen_arvo_2 = (paivien_maara // 2)
        keskimmaisten_keskiarvo = (paivat[pariton_keskimmainen_arvo_1] +
                                   paivat[pariton_keskimmainen_arvo_2]) / 2
        mediaani = keskimmaisten_keskiarvo

    print(f"Temperature median: {mediaani:.1f}C")


def laske_keskiarvo(paivat, paivien_maara):
    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    alkiot_yhteensa = 0
    keskiarvo = 0
    paivataulukon_pituus = len(paivat)

    for indeksi in range(0, paivataulukon_pituus, 1):
        alkiot_yhteensa += paivat[indeksi]

    keskiarvo = alkiot_yhteensa / paivien_maara
    print(f"Temperature mean: {keskiarvo:.1f}C")


def onko_arvo_negatiivinen_tai_nolla(arvo):
    """Funktio tutkii, onko käyttäjän syöttämä arvo negatiivinen tai nolla.
    Mikäli on, palauttaa arvon True, muuten arvon False."""
    return arvo <= 0


def kay_paivat_lapi(paivien_maara):
    """Funktio ottaa parametrinä vastaan käyttäjän mainissa syöttämän arvon."""

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    nykyinen_paiva = 0
    paivat = []
    tyhja_taulukko = []

    # Jos käyttäjä syöttää 0 tai vähemmän päiviä, ohjelman suoritus keskeytyy
    # mainissa.
    if onko_arvo_negatiivinen_tai_nolla(paivien_maara):
        return 0, 0

    for paiva in range(1, paivien_maara + 1, 1):
        print("Enter day ", paiva, ". temperature in Celsius: ",
              sep="", end="")
        nykyinen_paiva = float(input())
        paivat.append(nykyinen_paiva)

    return paivat, paivien_maara

    # print("Päästiin tänne for-loopin jälkeen")
    # print("Listan arvot", paivat)


def main():
    """Mainin tehtävänä on huolehtia kaikkien muiden funktioiden kutsumisesta.
    Jokainen yksittäinen toiminto on oma funktionsa, jotta sitä voidaan
    kutsua """

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    paivat = []
    paivien_maara = 0
    tiedot_paivista = []

    paivien_maara = int(input("Enter amount of days: "))

    # Funktion paluuarvot otetaan talteen taulukkoon
    tiedot_paivista = kay_paivat_lapi(paivien_maara)

    # Jos taulukon 1. ja 2. indeksi ovat nollia, ohjelma suljetaan
    if tiedot_paivista[0] == 0 and tiedot_paivista[1] == 0:
        return

    # Mainin muuttujat päivitetään ajan tasalle käy_päivät_läpi funktion pa-
    # lauttamien arvojen perusteella
    paivat = tiedot_paivista[0]
    paivien_maara = tiedot_paivista[1]

    laske_keskiarvo(paivat, paivien_maara)
    laske_mediaani(paivat, paivien_maara)


if __name__ == "__main__":
    main()
