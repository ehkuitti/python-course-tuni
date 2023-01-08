"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma lukee arvoja ja syöttää niitä sanakirjaan. Laskee sanakirjan sanojen
määrän.
"""


def main():
    syote = ""
    sanakirja = {}
    splitattu_syote = []
    syotteen_pituus = 0
    splitatun_syotteen_pituus = 0
    i = 0

    print("Enter rows of text for word counting. Empty row to quit.")

    while True:

        syote = input()

        # Luuppi kaadetaan tyhjällä merkkijonolla, käytännössä pelkän enterin
        # syöttämisellä
        if syote == "":
            break

        sanat = syote.split()

        for sana in sanat:
            if sana.lower() not in sanakirja:
                sanakirja[sana.lower()] = 1
            else:
                sanakirja[sana.lower()] += 1

    sortattu_sanakirja = dict(sorted(sanakirja.items()))

    for sana, arvo in sortattu_sanakirja.items():
        print(f"{sana} : {arvo} times")


if __name__ == "__main__":
    main()
