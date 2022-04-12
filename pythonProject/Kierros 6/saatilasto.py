"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def laske_keskiarvo(paivat, paivien_maara):

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    alkiot_yhteensa = 0
    keskiarvo = 0
    paivataulukon_pituus = len(paivat)

    for indeksi in range(0, paivataulukon_pituus, 1):
        alkiot_yhteensa += paivat[indeksi]

    keskiarvo = alkiot_yhteensa / paivien_maara
    print(f"Keskiarvo on: {keskiarvo:.2f}")


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

    for paiva in range(1, paivien_maara+1, 1):
        print("Enter day ", paiva, ". temperature in Celsius: ",
              sep="", end="")
        nykyinen_paiva = float(input())
        paivat.append(nykyinen_paiva)

    # laske_keskiarvo(paivat, paivien_maara)
    return paivat, paivien_maara

    # print("Päästiin tänne for-loopin jälkeen")
    # print("Listan arvot", paivat)


def main():

    paivat = []
    paivien_maara = 0
    tiedot_paivista = []

    paivien_maara = int(input("Enter amount of days: "))
    tiedot_paivista[0:1] = kay_paivat_lapi(paivien_maara)

    paivat = tiedot_paivista[0]
    paivien_maara = tiedot_paivista[1]

    laske_keskiarvo(paivat, paivien_maara)


if __name__ == "__main__":
    main()
