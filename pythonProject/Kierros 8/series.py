"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():

    sarjat = []
    sarjan_genret = ""
    sarjan_genret_splitattuna = []
    sarjan_genret_splitattuna_pituus = 0
    genresetti = set()
    genresetti_aakkosjarjestyksessa = set()
    genresetti_aakkosjarjestyksessa_merkkijonona = ""
    tiedostonimi = ""

    tiedostonimi = input("Enter the name of the file: ")

    try:
        tiedosto = open(tiedostonimi, mode="r")

    except OSError:
        print(f"Error: opening the file '{tiedostonimi}' failed!")
        return

    print("Available genres are: ", sep="", end="")

    i = 0
    for rivi in tiedosto:

        # Splitataan tiedosto puolipisteen kohdalta
        sarjat = rivi.split(";")

        # Sajran genret sijaitsevat splitin jälkeen indeksissä 1. Lopun
        # .stripillä leikataan rivinvaihto pois syötteestä.
        sarjan_genret = sarjat[1].strip()

        # Genret splitataan, jotta niitä voidaan käsitellä
        sarjan_genret_splitattuna = sarjan_genret.split(",")
        sarjan_genret_splitattuna_pituus = len(sarjan_genret_splitattuna)

        # Lisätään indeksistä i löytyvä genre genresettiin
        for i in range(0, sarjan_genret_splitattuna_pituus, 1):
            genresetti.add(sarjan_genret_splitattuna[i])
            # print(i, ":", genresetti)

    genresetti_aakkosjarjestyksessa = sorted(genresetti)
    genresetti_aakkosjarjestyksessa_merkkijonona = ", ".join\
        (genresetti_aakkosjarjestyksessa)

    print(genresetti_aakkosjarjestyksessa_merkkijonona)

    # for arvo in genresetti_aakkosjarjestyksessa:
    #     print(arvo, ", ", sep="", end="")

    # print(sarjan_genret_splitattuna)


if __name__ == "__main__":
    main()
