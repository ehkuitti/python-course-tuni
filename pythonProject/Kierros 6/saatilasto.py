"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def onko_arvo_kelvollinen(arvo):

    return arvo <= 0


def kay_paivat_lapi(paivien_maara):

    buuleani = False
    buuleani = onko_arvo_kelvollinen(arvo)
    print("Buuleani: ", buuleani)

    paivat = []


def main():

    paivien_maara = 0

    paivien_maara = int(input("Enter amount of days: "))
    kay_paivat_lapi(paivien_maara)

if __name__ == "__main__":
    main()
