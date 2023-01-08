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
    sarjan_nimi = ""
    syote = ""
    genresetti = set()
    genresetti_aakkosjarjestyksessa = set()
    genresetti_aakkosjarjestyksessa_merkkijonona = ""
    vastaavat_sarjat = []
    tiedostonimi = ""
    loydetty_oikea_sarja = False
    kategoriasetti = set()
    kategoriasetti_aakkosjarjestyksessa_merkkijonona = ""

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
    genresetti_aakkosjarjestyksessa_merkkijonona = ", ".join \
        (genresetti_aakkosjarjestyksessa)

    print(genresetti_aakkosjarjestyksessa_merkkijonona)

    print("> ", sep="", end="")

    syote = input()

    if syote == "exit":
        return

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
        sarjan_nimi = sarjat[0]

        if syote == sarjan_nimi:
            loydetty_oikea_sarja = True
            # vastaavat_sarjat.append(sarjan_nimi)

        # Genret splitataan, jotta niitä voidaan käsitellä
        sarjan_genret_splitattuna = sarjan_genret.split(",")
        sarjan_genret_splitattuna_pituus = len(sarjan_genret_splitattuna)

        # Lisätään indeksistä i löytyvä genre genresettiin
        if loydetty_oikea_sarja:
            for i in range(0, sarjan_genret_splitattuna_pituus, 1):
                kategoriasetti.add(sarjan_genret_splitattuna[i])
                # print(i, ":", genresetti)
            break
        else:
            continue

    kategoriasetti_aakkosjarjestyksessa = sorted(kategoriasetti)
    kategoriasetti_aakkosjarjestyksessa_merkkijonona = ", ".join \
        (kategoriasetti_aakkosjarjestyksessa)

    print(kategoriasetti_aakkosjarjestyksessa_merkkijonona)


if __name__ == "__main__":
    main()
