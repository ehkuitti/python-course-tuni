"""
COMP.CS.100 Tehtävä päivämäärät
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""


def main():

    kuukausi = 1
    pvm = 1

    while kuukausi <= 12:

        # Tapaus helmikuu
        if kuukausi == 2:
            while pvm <= 28:
                print(pvm, ".", kuukausi, ".", sep="")
                pvm += 1

        # Tapauksissa huhtikuu, kesäkuu, syyskuu, ja marraskuu on vain 30 päivää
        elif (kuukausi == 4) or (kuukausi == 6) or (kuukausi == 9) or (kuukausi == 11):
            while pvm <= 30:
                print(pvm, ".", kuukausi, ".", sep="")
                pvm += 1

        # Muissa kuukausissa on 31 päivää
        else:
            while pvm <= 31:
                print(pvm, ".", kuukausi, ".", sep="")
                pvm += 1

        pvm = 1
        kuukausi += 1;


if __name__ == "__main__":
    main()