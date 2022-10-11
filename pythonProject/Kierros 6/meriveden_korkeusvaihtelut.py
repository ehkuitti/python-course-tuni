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
    Keskiarvo lasketaan jakamalla alkioiden summa niiden määrällä, joka on
    tässä tapauksessa listan pituus. Palauttaa lasketun keskiarvon. """

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    keskiarvo = 0
    lista_alkioiden_summa = 0
    korkeusvaihtelulistan_pituus = len(korkeusvaihtelut)

    for indeksi in range(0, korkeusvaihtelulistan_pituus, 1):
        lista_alkioiden_summa += korkeusvaihtelut[indeksi]

    keskiarvo = lista_alkioiden_summa / korkeusvaihtelulistan_pituus
    return keskiarvo


def onko_arvo_pariton(arvo):
    """Funktion tarkoituksena on tarkistaa, onko annettu arvo pariton. Tämä
    tehdään jakamalla arvo kahdella ja tutkimalla jääkö jakojäännöstä, ts.
    meneekö jako tasan. Mikäli jako ei mene tasan, palauttaa Truen, jolloin lu-
    ku on pariton. Muussa tapauksessa polauttaa Falsen, jolloin luku
    on parillinen. """

    return arvo % 2 > 0


def laske_mediaani(korkeusvaihtelut):
    """Funktio laskee mediaanin annetuista arvoista. Ottaa parametreina vastaan
        paivalistan (jossa arvot tallessa) sekä päivien määrän (kokonaisluku).
        Funktiossa käytetään listan käsittelyyn nousevaan järjestykseen
        sortattua listan kopiota, jotta mediaanilaskut menevät oikein. Tähän
        EI käytetä .sort():tiam, jotta voidaan laskea keskiarvon ero
        mediaanin myöhemmin ohjelmassa. Palauttaa lasketun mediaanin.

        Mediaanin laskeminen:
        - Jos alkioita on pariton määrä, mediaani on
          paivat_pienimmasta_suurimpaan listan keskimmäinen alkio
        - Jos parillinen, se on kahden keskimmäisen arvon keskiarvo.
        """

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    keskimmaisten_keskiarvo = 0
    korkeusvaihteluiden_maara = len(korkeusvaihtelut)
    mediaani = 0
    korkeusvaihtelut_pienimmasta_suurimpaan = sorted(korkeusvaihtelut)
    parillinen_keskimmainen_arvo_1 = 0
    parillinen_keskimmainen_arvo_2 = 0
    pariton_keskimmainen_arvo = 0

    if onko_arvo_pariton(korkeusvaihteluiden_maara):

        # Keskimmainen sijaitsee taulukon puolivälissä
        pariton_keskimmainen_arvo = (korkeusvaihteluiden_maara // 2)
        mediaani = \
            korkeusvaihtelut_pienimmasta_suurimpaan[pariton_keskimmainen_arvo]

    else:

        # Otetaan muuttujiin talteen kaksi keskimmäistä arvoa sekä niiden
        # keskiarvo
        parillinen_keskimmainen_arvo_1 = (korkeusvaihteluiden_maara // 2) - 1
        parillinen_keskimmainen_arvo_2 = (korkeusvaihteluiden_maara // 2)
        keskimmaisten_keskiarvo = (korkeusvaihtelut_pienimmasta_suurimpaan
                                   [parillinen_keskimmainen_arvo_1] +
                                   korkeusvaihtelut_pienimmasta_suurimpaan
                                   [parillinen_keskimmainen_arvo_2]) / 2
        mediaani = keskimmaisten_keskiarvo

    return mediaani


def main():
    # MUUTTUJIEN ALUSTUKSET MUUTTUJATYYPEITTÄIN AAKKOSJÄRJESTYKSESSÄ

    # Kokonaisluvut
    i = 0

    # Listat
    korkeusvaihtelut = []

    # Liukuluvut
    keskiarvo = 0.0
    maksimiarvo = 0.0
    mediaani = 0.0
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
    mediaani = laske_mediaani(korkeusvaihtelut)
    keskiarvo = laske_keskiarvo(korkeusvaihtelut)

    print(f"Minimum: {minimiarvo:.2f} cm")
    print(f"Maximum: {maksimiarvo:.2f} cm")
    print(f"Median: {mediaani:.2f} cm")
    print(f"Mean: {keskiarvo:.2f} cm")


if __name__ == "__main__":
    main()
