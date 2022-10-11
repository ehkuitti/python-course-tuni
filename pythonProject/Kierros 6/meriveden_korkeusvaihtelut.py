"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def laske_minimiarvo(korkeusvaihtelut):
    """Funktio ottaa parametrina vastaan listan, jossa korkeusvaihtelut ovat.
    Funktio min etsii sieltä pienimmän arvon, jonka jälkeen funktio palauttaa
    tämän arvon."""

    minimi_korkeusvaihtelu = min(korkeusvaihtelut)
    return minimi_korkeusvaihtelu


def laske_maksimiarvo(korkeusvaihtelut):
    """Funktio ottaa parametrina vastaan listan, jossa korkeusvaihtelut ovat.
    Funktio max etsii sieltä suurimman arvon, jonka jälkeen funktio palauttaa
    tämän arvon."""

    maksimi_korkeusvaihtelu = max(korkeusvaihtelut)
    return maksimi_korkeusvaihtelu


def laske_keskiarvo(korkeusvaihtelut):
    """Funktio ottaa parametrinä listan, jossa käsiteltävät arvot ovat, sekä
    Keskiarvo lasketaan jakamalla alkioiden summa niiden määrällä.
    Palauttaa keskiarvon mainille. """

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    keskiarvo = 0
    lista_alkioiden_summa = 0
    korkeusvaihtelulistan_pituus = len(korkeusvaihtelut)

    for indeksi in range(0, korkeusvaihtelulistan_pituus, 1):
        lista_alkioiden_summa += korkeusvaihtelut[indeksi]

    keskiarvo = lista_alkioiden_summa / korkeusvaihtelulistan_pituus
    return keskiarvo


def main():
    # MUUTTUJIEN ALUSTUKSET MUUTTUJATYYPEITTÄIN AAKKOSJÄRJESTYKSESSÄ

    # Kokonaisluvut
    i = 0

    # Listat
    korkeusvaihtelut = []

    # Liukuluvut
    keskiarvo = 0.0
    maksimiarvo = 0.0
    minimiarvo = 0.0
    syotetty_arvo = 0.0

    # Merkkijonot
    str_syotetty_arvo = ""
    stripattu_str_syotetty_arvo = ""

    # Totuusarvot
    onko_syote_numero = True

    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")

    while onko_syote_numero:
        str_syotetty_arvo = input()

        # Varmistetaan, että myös pelkän välilyönnin syöttäminen vastaa
        # tyhjän arvon syöttämistä
        stripattu_str_syotetty_arvo = str_syotetty_arvo.strip()

        if stripattu_str_syotetty_arvo == "" and i < 3:
            print("Error: At least two measurements must be entered.")
            return 1

        elif stripattu_str_syotetty_arvo == "" and i > 3:
            onko_syote_numero = False
            # Tämän jälkeen whilen ulkopuolella tulostetaan yhteenveto arvoista

        else:
            syotetty_arvo = float(stripattu_str_syotetty_arvo)
            korkeusvaihtelut.append(syotetty_arvo)

        i += 1

    # Tähän tultaessa arvojen syöttäminen on päättynyt, joten voidaan
    # tulostaa kaikki halutut tulokset. Tämä tapahtuu ottamaan talteen
    # kutankin arvoa vastaavan funktion paluuarvot ja tulostamalla ne.

    minimiarvo = laske_minimiarvo(korkeusvaihtelut)
    maksimiarvo = laske_maksimiarvo(korkeusvaihtelut)
    keskiarvo = laske_keskiarvo(korkeusvaihtelut)

    print(f"Minimum: {minimiarvo:.2f}")
    print(f"Maximum: {maksimiarvo:.2f}")
    print(f"Mean: {keskiarvo:.2f}")


if __name__ == "__main__":
    main()
