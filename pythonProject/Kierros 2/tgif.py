"""
COMP.CS.100 Tehtävä päivämäärät
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""


def main():
    kuukausi = 1
    pvm = 3
    i = 0
    while kuukausi <= 12:

        # Tapaus helmikuu
        if kuukausi == 2:
            while pvm <= 28:
                if i % 7 == 0:
                    print(pvm, ".", kuukausi, ".", sep="")
                pvm += 1
                i += 1


        # Tapauksissa huhtikuu, kesäkuu, syyskuu, ja marraskuu on vain 30 päivää
        elif (kuukausi == 4) or (kuukausi == 6) or (kuukausi == 9) or (kuukausi == 11):
            while pvm <= 30:
                if i % 7 == 0:
                    print(pvm, ".", kuukausi, ".", sep="")
                pvm += 1
                i += 1


        # Muissa kuukausissa on 31 päivää
        else:
            while pvm <= 31:
                if i == 0 or i % 7 == 0:
                    print(pvm, ".", kuukausi, ".", sep="")
                pvm += 1
                i += 1

        pvm = 1
        kuukausi += 1


if __name__ == "__main__":
    main()
