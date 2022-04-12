"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def onko_arvo_negatiivinen_tai_nolla(arvo):
    """Funktio tutkii, onko käyttäjän syöttämä arvo negatiivinen tai nolla.
    Mikäli on, palauttaa arvon True, muuten arvon False."""
    return arvo <= 0


def kay_paivat_lapi(paivien_maara):
    """Funktio ottaa parametrinä vastaan käyttäjän mainissa syöttämän arvon."""

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    nykyinen_paiva = 0
    paivat = []

    # Jos käyttäjä syöttää 0 tai vähemmän päiviä, ohjelman suoritus keskeytyy
    if onko_arvo_negatiivinen_tai_nolla(paivien_maara):
        return

    for i in range(1, paivien_maara+1, 1):
        print("Enter day ", i, ". temperature in Celsius: ", sep="", end="")
        nykyinen_paiva = int(input())
        paivat.append(nykyinen_paiva)

    # print("Päästiin tänne for-loopin jälkeen")
    # print("Listan arvot", paivat)


def main():

    paivien_maara = 0

    paivien_maara = int(input("Enter amount of days: "))
    kay_paivat_lapi(paivien_maara)


if __name__ == "__main__":
    main()
