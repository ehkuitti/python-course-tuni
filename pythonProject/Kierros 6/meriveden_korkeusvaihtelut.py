"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def minimiarvo(korkeusvaihtelut):
    """Funktio ottaa parametrina vastaan listan, jossa korkeusvaihtelut ovat.
    Funktio min etsii sieltä pienimmän arvon, jonka jälkeen funktio palauttaa
    tämän arvon."""
    minimi_korkeusvaihtelu = min(korkeusvaihtelut)
    return minimi_korkeusvaihtelu


def maksimiarvo(korkeusvaihtelut):
    """Funktio ottaa parametrina vastaan listan, jossa korkeusvaihtelut ovat.
    Funktio max etsii sieltä suurimman arvon, jonka jälkeen funktio palauttaa
    tämän arvon."""
    maksimi_korkeusvaihtelu = max(korkeusvaihtelut)
    return maksimi_korkeusvaihtelu


def main():
    # MUUTTUJIEN ALUSTUKSET MUUTTUJATYYPEITTÄIN AAKKOSJÄRJESTYKSESSÄ

    # Kokonaisluvut
    i = 0

    # Listat
    korkeusvaihtelut = []

    # Liukuluvut
    maksimi = 0.0
    minimi = 0.0
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

    # Tähän tultaessa arvojen syöttäminen on päättynyt, joten voidaan
    # tulostaa kaikki halutut tulokset. Tämä tapahtuu ottamaan talteen
    # kutankin arvoa vastaavan funktion paluuarvot ja tulostamalla ne.

    minimi = minimiarvo(korkeusvaihtelut)
    maksimi = maksimiarvo(korkeusvaihtelut)

    print(f"Minimum: {minimi:.1f}")
    print(f"Maksimi: {maksimi:.1f}")


if __name__ == "__main__":
    main()
