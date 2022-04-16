"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():
    i = 0
    input_taulukko = []
    sanakirja_tulostaulu = {}
    syote = ""
    syote_pienilla_kirjaimilla = ""
    splitattu_pienten_kirjainten_syote = ""

    print("Enter rows of text for word counting. Empty row to quit.")
    syote = input()

    while syote != "":
        syote = input()
        syote_pienilla_kirjaimilla = syote.lower()
        splitattu_pienten_kirjainten_syote = syote_pienilla_kirjaimilla.split()
        input_taulukko.append(splitattu_pienten_kirjainten_syote)

    while i < len(input_taulukko):

        if input_taulukko[i] not in sanakirja_tulostaulu:
            sanakirja_tulostaulu[input_taulukko[i]] = \
                input_taulukko[i]

        i += 1

    print("Tulostaulu: ", sanakirja_tulostaulu)


if __name__ == "__main__":
    main()
