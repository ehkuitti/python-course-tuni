"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def create_an_acronym(sana_josta_tehdaan_akronyymi):
    """Tämä funktio luo akronyymejä leikkaamalla annetun stringin
    sanojen muut kirjaimet paitsi ekan pois, poistamalla välilyönnit
    ja muuttamalla ne isoiksi kirjaimiksi."""
    akronyymi = ""
    alkuperainen_splitattu_merkkitaulukko = ""
    suuremman_luokan_kirjain = ""

    sanan_pituus = len(sana_josta_tehdaan_akronyymi)

    if sanan_pituus == 0 or sanan_pituus == 1:
        suuremman_luokan_kirjain = sana_josta_tehdaan_akronyymi.upper()
        return suuremman_luokan_kirjain

    kenttataulukko = []
    sana_kentta_1 = 0
    sana_kentta_2 = 0
    sana_kentta_3 = 0
    sana_kentta_4 = 0
    sana_kentta_5 = 0
    sana_kentta_6 = 0
    sana_kentta_7 = 0
    sana_kentta_8 = 0
    sana_kentta_9 = 0
    sana_kentta_10 = 0

    sana_kentta_1_eka_kirjain = ""
    sana_kentta_2_eka_kirjain = ""
    sana_kentta_3_eka_kirjain = ""
    sana_kentta_4_eka_kirjain = ""
    sana_kentta_5_eka_kirjain = ""
    sana_kentta_6_eka_kirjain = ""
    sana_kentta_7_eka_kirjain = ""
    sana_kentta_8_eka_kirjain = ""
    sana_kentta_9_eka_kirjain = ""
    sana_kentta_10_eka_kirjain = ""

    sana_kentta_1_eka_kirjain_isona = ""
    sana_kentta_2_eka_kirjain_isona = ""
    sana_kentta_3_eka_kirjain_isona = ""
    sana_kentta_4_eka_kirjain_isona = ""
    sana_kentta_5_eka_kirjain_isona = ""
    sana_kentta_6_eka_kirjain_isona = ""
    sana_kentta_7_eka_kirjain_isona = ""
    sana_kentta_8_eka_kirjain_isona = ""
    sana_kentta_9_eka_kirjain_isona = ""
    sana_kentta_10_eka_kirjain_isona = ""

    if sanan_pituus < 28:
        alkuperainen_splitattu_merkkitaulukko = \
            sana_josta_tehdaan_akronyymi.split(" ")
        sana_kentta_1 = alkuperainen_splitattu_merkkitaulukko[0]
        sana_kentta_2 = alkuperainen_splitattu_merkkitaulukko[1]
        sana_kentta_3 = alkuperainen_splitattu_merkkitaulukko[2]

        sana_kentta_1_eka_kirjain = sana_kentta_1[0]
        sana_kentta_2_eka_kirjain = sana_kentta_2[0]
        sana_kentta_3_eka_kirjain = sana_kentta_3[0]

        sana_kentta_1_eka_kirjain_isona = sana_kentta_1_eka_kirjain.upper()
        sana_kentta_2_eka_kirjain_isona = sana_kentta_2_eka_kirjain.upper()
        sana_kentta_3_eka_kirjain_isona = sana_kentta_3_eka_kirjain.upper()

        akronyymi = sana_kentta_1_eka_kirjain_isona + \
                    sana_kentta_2_eka_kirjain_isona + \
                    sana_kentta_3_eka_kirjain_isona
        return akronyymi

    else:
        alkuperainen_splitattu_merkkitaulukko = \
            sana_josta_tehdaan_akronyymi.split(" ")
        sana_kentta_1 = alkuperainen_splitattu_merkkitaulukko[0]
        sana_kentta_2 = alkuperainen_splitattu_merkkitaulukko[1]
        sana_kentta_3 = alkuperainen_splitattu_merkkitaulukko[2]
        sana_kentta_4 = alkuperainen_splitattu_merkkitaulukko[3]
        sana_kentta_5 = alkuperainen_splitattu_merkkitaulukko[4]
        sana_kentta_6 = alkuperainen_splitattu_merkkitaulukko[5]
        sana_kentta_7 = alkuperainen_splitattu_merkkitaulukko[6]
        sana_kentta_8 = alkuperainen_splitattu_merkkitaulukko[7]
        sana_kentta_9 = alkuperainen_splitattu_merkkitaulukko[8]
        sana_kentta_10 = alkuperainen_splitattu_merkkitaulukko[9]

        sana_kentta_1_eka_kirjain = sana_kentta_1[0]
        sana_kentta_2_eka_kirjain = sana_kentta_2[0]
        sana_kentta_3_eka_kirjain = sana_kentta_3[0]
        sana_kentta_4_eka_kirjain = sana_kentta_4[0]
        sana_kentta_5_eka_kirjain = sana_kentta_5[0]
        sana_kentta_6_eka_kirjain = sana_kentta_6[0]
        sana_kentta_7_eka_kirjain = sana_kentta_7[0]
        sana_kentta_8_eka_kirjain = sana_kentta_8[0]
        sana_kentta_9_eka_kirjain = sana_kentta_9[0]
        sana_kentta_10_eka_kirjain = sana_kentta_10[0]

        sana_kentta_1_eka_kirjain_isona = sana_kentta_1_eka_kirjain.upper()
        sana_kentta_2_eka_kirjain_isona = sana_kentta_2_eka_kirjain.upper()
        sana_kentta_3_eka_kirjain_isona = sana_kentta_3_eka_kirjain.upper()
        sana_kentta_4_eka_kirjain_isona = sana_kentta_4_eka_kirjain.upper()
        sana_kentta_5_eka_kirjain_isona = sana_kentta_5_eka_kirjain.upper()
        sana_kentta_6_eka_kirjain_isona = sana_kentta_6_eka_kirjain.upper()
        sana_kentta_7_eka_kirjain_isona = sana_kentta_7_eka_kirjain.upper()
        sana_kentta_8_eka_kirjain_isona = sana_kentta_8_eka_kirjain.upper()
        sana_kentta_9_eka_kirjain_isona = sana_kentta_9_eka_kirjain.upper()
        sana_kentta_10_eka_kirjain_isona = sana_kentta_10_eka_kirjain.upper()

        akronyymi = sana_kentta_1_eka_kirjain_isona + \
                    sana_kentta_2_eka_kirjain_isona + \
                    sana_kentta_3_eka_kirjain_isona + \
                    sana_kentta_4_eka_kirjain_isona + \
                    sana_kentta_5_eka_kirjain_isona + \
                    sana_kentta_6_eka_kirjain_isona + \
                    sana_kentta_7_eka_kirjain_isona + \
                    sana_kentta_8_eka_kirjain_isona + \
                    sana_kentta_9_eka_kirjain_isona + \
                    sana_kentta_10_eka_kirjain_isona

    return akronyymi

def main():
    akronyymi = ""
    sana = ""
    sana = input("Input a word for which you'd like to create an acronym: ")

    akronyymi = create_an_acronym(sana)
    print(akronyymi)


if __name__ == "__main__":
    main()
