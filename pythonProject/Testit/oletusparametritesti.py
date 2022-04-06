"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def opiskelija(lkm, reaktio="hätkähdä", homma="ohjelmointi",
               toimet="ryhtyisi toimeen"):
    print("Tämä opiskelija ei ", reaktio, " vaikka antaisit sille ", lkm, " ",
          homma, "tehtävää, vaan ", toimet, ".", sep="")


def main():
    opiskelija(100)
    opiskelija(reaktio="pelästyisi", lkm=1000)
    opiskelija("tuhat", toimet="alkaisi integroida", homma="lasku")
    opiskelija("miten monta", "korvaansa lotkauttaisi", "siivous",
               "jatkaisi tietokoneensa räpläämistä")


if __name__ == "__main__":
    main()
