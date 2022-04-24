"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def read_file(str_tiedostonimi):
    """Lukee tiedostosta rivejä sanakirjaan. Sanakirjaan tallennetaan
    avaimeksi rivin avain ja pariksi sanakirja, jossa loput tiedot."""

    # MUUTTUJIEN ALUSTUKSET (TYYPPEINEEN, AAKKOSJÄRJESTYKSESSÄ)

    # Listat
    lst_tiedostorivi_splitattuna = []

    # Merkkijonot
    # str_tiedostonimi = ""

    # Sanakirjat
    dict_yhteystiedot = {}
    dict_arvot = {}

    try:
        tiedosto = open(str_tiedostonimi, mode="r")

    except OSError:
        print(f"Virhe: Tiedostoa nimellä {str_tiedostonimi} ei löytynyt.")
        return

    for rivi in tiedosto:
        str_tiedostonimi_stripattuna = rivi.strip()
        lst_tiedostorivi_splitattuna = str_tiedostonimi_stripattuna.split(";")

        solu_avain = lst_tiedostorivi_splitattuna[0]
        solu_nimi = lst_tiedostorivi_splitattuna[1]
        solu_puhnro = lst_tiedostorivi_splitattuna[2]
        solu_meili = lst_tiedostorivi_splitattuna[3]
        solu_skype = lst_tiedostorivi_splitattuna[4]

        dict_arvot["name"] = solu_nimi
        dict_arvot["phone"] = solu_puhnro
        dict_arvot["email"] = solu_meili
        dict_arvot["skype"] = solu_skype

        # Tiedot tallennetaan pariksi sanakirjaan. Avaimena toimii rivin
        # avain ja parina on sanakirja, josta löytyy loput tiedot.

        dict_yhteystiedot[solu_avain] = dict_arvot.copy()

    # for avain, sanakirja in dict_yhteystiedot.items():
    #
    #     if avain == haettavan_henkilon_nimi:
    #         for sisainen_avain, sisainen_arvo in dict_arvot.items():
    #             if sisainen_avain == haettava_asia:
    #                 pass

    return dict_yhteystiedot

def main():

    tiedostonimi = ""
    nimi = ""
    haettava_asia = ""

    tiedostonimi = input("Anna tiedostonimi: ")
    nimi = input("Anna henkilön nimi: ")
    puhnro = input("Anna haettava asia: ")

    paluuarvo = read_file(tiedostonimi)
    print(paluuarvo)


if __name__ == "__main__":
    main()
