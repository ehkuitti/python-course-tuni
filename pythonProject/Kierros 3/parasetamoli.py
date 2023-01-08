"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelman tarkoitus on annostella parasetamolia potilaalle.
"""

YKSITTAINEN_ANNOS = 15
PAIVITTAINEN_MAKSIMIANNOS = 4000


def calculate_dose(str_paino, str_aika, str_annos_viimeiset_24h):
    """Laskee oikean annoksen annettujen parametrien perusteella"""
    # Muutetaan arvot kokonaisluvuiksi, jotta niillä voidaan tehdä matemaatti-
    # sia operaatioita
    paino = int(str_paino)
    aika = int(str_aika)
    annos_viimeiset_24h = int(str_annos_viimeiset_24h)

    # Omat muuttujat
    annettava_annos = 1
    annettu_kerta_annos = 1
    jaljella_annettavaa = 1
    kuluneet_annoskerrat = 0
    maksimi_kerta_annos = paino * 15
    maksimi_vuorokausiannos = 4000
    voidaanko_laaketta_antaa = True

    if aika < 6:
        voidaanko_laaketta_antaa = False

    if annos_viimeiset_24h == 4000:
        voidaanko_laaketta_antaa = False

    # print("Kuluneet annoskerrat: ", kuluneet_annoskerrat)
    # print("Maksimi kerta-annos: ", maksimi_kerta_annos)

    if maksimi_kerta_annos * 4 > 4000:
        maksimi_vourokausiannos = 4000
    else:
        maksimi_vuorokausiannos = maksimi_kerta_annos * 4

    # print("Maksimi vuorokausiannos: ", maksimi_vourokausiannos)
    # print("Annos viimeiset 24h: ", annos_viimeiset_24h)

    jaljella_annettavaa = maksimi_vuorokausiannos - annos_viimeiset_24h

    # print("Jäljellä annettavaa: ", jaljella_annettavaa)
    if jaljella_annettavaa >= maksimi_kerta_annos:
        annettava_annos = maksimi_kerta_annos

    elif jaljella_annettavaa <= maksimi_kerta_annos:
        annettava_annos = jaljella_annettavaa

    if voidaanko_laaketta_antaa is True:
        return annettava_annos

    else:
        return 0


def main():
    paino = 0
    aika_edellisesta = 0
    annos_viimeiset_24h = 0
    annettava_annos = 0

    paino = int(input("Patient's weight (kg): "))
    aika_edellisesta = int(input("How much time has passed from the previous "
                                 "dose (full hours): "))
    annos_viimeiset_24h = int(input("The total dose for the last "
                                    "24 hours (mg): "))
    annettava_annos = \
        calculate_dose(paino, aika_edellisesta, annos_viimeiset_24h)

    print("The amount of Parasetamol to give to the patient:", annettava_annos)


if __name__ == "__main__":
    main()

# "The amount of Parasetamol to give to the patient: "
