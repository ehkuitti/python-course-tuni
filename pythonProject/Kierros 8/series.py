"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():
    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPEITTÄIN)

    # KOKONAISLUVUT
    int_genret_splitattuna_pituus = 0

    # LISTAT
    lst_sarjat_genreineen = []
    lst_genret_splitattuna = []

    # MERKKIJONOT
    str_tiedostonimi = ""
    str_stripattu_nimi = ""
    str_stripatut_genret = ""
    str_syote = ""
    genre = ""

    # SANAKIRJAT
    dict_sarjat_genreineen = {}

    # SETIT
    genresetti = set()

    str_tiedostonimi = input("Enter the name of the file: ")

    try:
        tiedosto = open(str_tiedostonimi, mode="r")

    except OSError:
        print(f"Error: opening the file '{str_tiedostonimi}' failed!")
        return

    for rivi in tiedosto:

        # Splitataan tiedosto puolipisteen kohdalta: Indeksiin 0 tulee sarjan
        # nimi, indeksiin 1 genret.
        lst_sarjat_genreineen = rivi.split(";")

        # Poistaa rivinvaihdon rivin lopusta
        str_stripattu_nimi = lst_sarjat_genreineen[0].strip()
        str_stripatut_genret = lst_sarjat_genreineen[1].strip()

        # Splitataan genret pilkun kohdalta .splitillä, palauttaa listan.
        lst_genret_splitattuna = str_stripatut_genret.split(",")
        int_genret_splitattuna_pituus = len(lst_genret_splitattuna)

        # Lisätään nimi ja taulukko (lista) parina sanakirjaan
        if str_stripattu_nimi not in dict_sarjat_genreineen:
            dict_sarjat_genreineen[str_stripattu_nimi] = lst_genret_splitattuna

        # Tehdään setti valmiiksi alun tulostusta varten
        for i in range(0, int_genret_splitattuna_pituus, 1):
            genresetti.add(lst_genret_splitattuna[i])

    genresetti_aakkosjarjestyksessa = sorted(genresetti)
    str_genresetti_aakkosjarjestyksessa = ", ".join \
        (genresetti_aakkosjarjestyksessa)

    print("Available genres are: ", sep="", end="")
    print(str_genresetti_aakkosjarjestyksessa)

    while True:
        print("> ", sep="", end="")
        str_syote = input()

        if str_syote == "exit":
            break

        else:
            for sarja in sorted(dict_sarjat_genreineen):
                for genre in sorted(dict_sarjat_genreineen[sarja]):
                    if genre == str_syote:
                        print(sarja)


                # if genre == str_syote:
                #     # for genre in sorted(dict_sarjat_genreineen[sarja]):
                #     print(sarja)


                # print(dict_sarjat_genreineen)

        # print(dict_sarjat_genreineen)


if __name__ == "__main__":
    main()
