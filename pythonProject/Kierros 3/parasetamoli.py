"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelman tarkoitus on annostella parasetamolia potilaalle.
"""

YKSITTAINEN_ANNOS = 15


def calculate_dose(str_paino, str_aika, str_annos_viimeiset_24h):
    """Laskee oikean annoksen annettujen parametrien perusteella"""
    # Muutetaan arvot kokonaisluvuiksi, jotta niillä voidaan tehdä matemaatti-
    # sia operaatioita
    paino = int(str_paino)
    aika = int(str_aika)
    annos_viimeiset_24h = int(str_annos_viimeiset_24h)

    # Omia muuttujia
    voidaanko_taysi_annos_antaa = True
    kokonaisannos = 0

    # Jos lihava
    if (paino * YKSITTAINEN_ANNOS) > 4000:
        voidaanko_taysi_annos_antaa = False

    return kokonaisannos


def main():
    paino, aika, annos_viimeiset_24h = 0

    paino = int(input("Patient's weight (kg): "))
    aika = int(input("How much time has passed from the previous dose "
                     "(full hours): "))
    annos_viimeiset_24h = int(input("The total dose for the last "
                                    "24 hours (mg): "))


if __name__ == "__main__":
    main()

# "The amount of Parasetamol to give to the patient: "
