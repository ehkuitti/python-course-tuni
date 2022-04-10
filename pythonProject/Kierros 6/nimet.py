"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelman tarkoituksena on kääntää käyttäjän syöttämiä nimiä toisinpäin.
"""


def reverse_name(syote):
    """Funktio ottaa parametrina käyttäjän antaman nimen, jota käsitellään.
    Normaalitilanteessa arvot annetaan \"<sukunimi>, <etunimi\" järjestyk-
    sessä. On kuitenkin muutama poikkeustilanne

    Poikkeustilanteita:
    Pilkku puuttuu: Palautetaan nimi itsessään eli kutsuparametrin arvo
    Toinen nimistä on tyhjä merkkijono tai välilyönti: Nimi stripataan väli-
    lyönneistä ja palautetaan se nimi, joka ei ollut tyhjää vastaava arvo."""

    # Muuttujien alustukset
    erotinmerkki = ","
    kentat = []
    kentta_sukunimi = 0
    kentta_etunimi = 0
    stripattu_etunimi = ""
    stripattu_sukunimi = ""
    sukunimi_on_tyhja = False
    etunimi_on_tyhja = False
    uusi_koko_nimi = ""

    # Jos syötetty nimi ei sisällä pilkkua
    if erotinmerkki not in syote:
        return syote

    else:
        kentat = syote.split(erotinmerkki)
        # print("Kentät indeksissä 0: ", kentat[0])
        # print("Kentät indeksissä 1: ", kentat[1])

    kentta_sukunimi = kentat[0]
    kentta_etunimi = kentat[1]

    if kentta_sukunimi == " " or kentta_sukunimi == "":
        sukunimi_on_tyhja = True

    elif kentta_etunimi == " " or kentta_etunimi == "":
        etunimi_on_tyhja = True

    if sukunimi_on_tyhja is True:
        stripattu_etunimi = kentta_etunimi.strip()
        return stripattu_etunimi

    elif etunimi_on_tyhja is True:
        stripattu_sukunimi = kentta_sukunimi.strip()
        return stripattu_sukunimi

    stripattu_sukunimi = kentta_sukunimi.strip()
    stripattu_etunimi = kentta_etunimi.strip()

    uusi_koko_nimi = stripattu_etunimi + " " + stripattu_sukunimi
    return uusi_koko_nimi


def main():
    syote = ""
    paluuarvo = ""

    syote = input("Input a name to be reversed: ")

    paluuarvo = reverse_name(syote)
    # print("Paluuarvo:", paluuarvo, end="")


if __name__ == "__main__":
    main()
